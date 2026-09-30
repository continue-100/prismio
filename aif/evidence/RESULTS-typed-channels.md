# Plain-data channels copy through the ring

**Status: DONE, 2026-09-30.** Apple Silicon (M-series, 4P+6E), LLVM 23. The
Phase 1 slice of `docs/CHANNELS_PLAN.md` that removes the per-message box for
messages of scalars, plus the method surface channels are written in now.

## The result

| measurement | before | after | C++ | Rust |
|---|---:|---:|---:|---:|
| `channel_pipeline`, `prismio bench`, 21 runs | 1.63x of C++ (2026-09-28) | **0.92x of C++** | 2.9 ms | 2.3 ms (after: 1.18x) |
| suite binary, in-process `elapsed_ns`, 31 alternating runs | 4.002 ms median | **2.606 ms** (0.651x) | | |
| standalone 3-stage pipeline, 5M messages, 21 alternating process runs | 1.025 s | **0.646 s** (0.630x) | 0.688 s (0.671x) | |
| same, user / sys | 0.593 s / 1.266 s | 0.292 s / 0.776 s | 0.343 s / 0.810 s | |
| `--verify` ledger, 1M messages | 2,000,001 allocated | **1 allocated** | | |

Checksums agree across every arm. The standalone pipeline bounds its generator
(`(i % 50000) * 25173`), because `i * 25173` overflows `Int` past ~85k messages
and the C++ arm's overflow is undefined; unbounded, the two printed different
checksums. The C probe's prediction (`.prismio/wip/channel_probe.c`, mode 2 at
0.58, C++ at ~0.61) held: 0.630 against C++'s 0.671 on the real compiler.

**Nothing else moved.** `tools/ir_snapshot.py` over `tests/`, `aif/corpus/`,
the benchmarks and `src/main.psm`, old compiler against new in one toolchain
layout: all 264 programs both compile are byte-identical. The four that differ
are the ones rewritten to the method surface, which the old compiler cannot
parse. In the suite binary, the only functions whose IR changed are `stage1`,
`stage2` and `benchChannelPipeline`; two more differ only in a source-path hash
inside a string constant's name.

## What was built

- **Runtime** (`runtime/program_support.c`): `chan_send_copy(c, src, size)` and
  `chan_recv_copy(c, dst, size)` over a lazily allocated byte ring beside the
  pointer ring. `recv` answers a status, so the destination is the caller's.
- **Sema**: `semaChannelCopies` routes a channel whose element is a non-generic
  struct of `INT`/`FLOAT`/`BOOL`/`CHAR` fields to the copy pair, and a copied
  send does not consume its value.
- **AIF**: `chan_recv_copy` is a produce site that is *not* foreign, so it is
  placed like a struct literal. The pipeline's receives are T0.
- **Codegen** (`generateChannelRecvCopy`): receive into a hoisted slot; at T0
  that slot is the value, and at any other tier it is copied into storage from
  the same ladder a struct literal uses (`allocPlacedStruct`, extracted from
  `generateStructLiteral` with identical emission). In test_232 a value held
  across iterations lands in a region arena and one pushed into a `Vec` in an
  `rc_alloc` block.
- **Layout**: hot/cold splitting is vetoed for a copied message type.
- **Surface** (`src/sema/channel.psm`): `Channel<T>(n)`, `c.send(v) -> Bool`,
  `c.receive()`, `for msg in c`, `c.share()`, `c.close()`, `c.length`,
  `c.free()`. The `chan_*` names are refused in source with the method they
  mean.

## Found on the way

- **The oracle never stripped `?` from a site type.** `aifSiteType` has done so
  in the compiler since `chan_recv`; `aif.py`'s `new_site` did not, so a
  received `Job?` was an `opaque` site there. That was invisible while `foreign`
  kept both sides off T0, and it surfaced as `T0: compiler=10 oracle=4` once the
  copy path lifted it. Fixed in the oracle; the differential agrees on all 19.
- **A received message leaked the fields it owned** (pre-existing, pointer
  path). `let taken = c.receive()` on a `Channel<Note { text: String }>` released
  with the plain deallocator, because `dropKindOf` reads a `T?` as `ptr`: 101
  allocated, 51 released, 50 leaked on the old compiler. `bindingDropKind` sees
  through the optional to the struct's generated release. test_232 is 208 / 208 / 0.
- **neg_56 would have passed vacuously.** Its `Job { seed: Int }` is plain data
  now, so the send copies and "use of moved value" no longer fires. Its message
  owns a String now.

## The pointer path's ledger (same day)

A send to a closed channel leaked the message it refused -- 21, 10 and 20 blocks
for ten refused `Note`, `String` and `Vec<Int>` sends -- because the send had
moved it and nobody owned it after. `generateUndeliveredRelease` releases it on
the `0` path with `valueDropKind`, the function a received `T?` is released by,
so a refused message is released exactly as its receiver would have released it.

Measuring that turned up three more defects on the same path, all pre-existing:

| probe | before | after |
|---|---|---|
| ten short Strings through a channel | every message read `s9`; 8+ "release of a pointer that is not live" (a stack address) | `s0`..`s9`, 11 / 11 / 0 |
| ten `Vec<Int>` round trips | 21 / 1 / 20 | 21 / 21 / 0 |
| refused `Note` sends in a program that also sends a `concat` String | no `__aif_release_Note` generated; every text leaked | released |
| test_235, all of the above | -- | 160 / 160 / 0 |

The last was `chan_send`'s `consume` contract marking the message's site
`transferred`. The flag means "the callee frees it" and has one reader,
`elem_disposition_of`, which answers NONE for such a site -- and a site is
shared: every `concat` in the program allocates in one place in std. A channel
frees nothing, so the send now keeps `no_stack` and the escape to Caller and
drops the mark; the binding it was sent from is still kept off the drop list by
the retained-argument note.

IR: every program in `tests/`, `aif/corpus/` and the benchmarks is byte-identical
to the previous compiler's except test_232, where `produceNotes` gains the
release branch and every other function differs only in label numbers (and
`src/main.psm`, which is the compiler being changed).

Left open, neither channel-specific: locals are keyed by function and name, so a
sent `v` and a received `v` in one function share a value set and the received
one leaks; and a string literal stored in a struct field turns off that field's
release for the whole type.

## Tried, and not levers

Measured in a C probe of the copy ring (`typed-channels/spin_probe.c`: `clang -O2`,
then `./spin_probe <spins> <yields> 5000000`; 5M messages, 7
interleaved rounds, ms):

| spin before parking | median |
|---|---:|
| none (what shipped) | 680 |
| 64 / 256 relax | 680 / 686 |
| 1024 relax | 663 |
| 4096 relax | 964 |
| 4 `sched_yield` / 256 relax + 4 yields | 662 / 661 |
| 1024 relax + 16 yields | 1083 |

At best 3%, and a cliff either side, which is crossbeam's own warning
(crossbeam-rs/crossbeam#821). macOS mutexes have been first-fit by default since
10.14, so the lock policy is not a lever. Waiter-counted signalling, a compare
for the wrap, and an SPSC ring were already negative (CHANNELS_PLAN §2,
`RESULTS-g9-channel-topology.md`).

**Not built:** a direct handoff into a parked receiver's slot, as Go's
`sendDirect` does. `chan_recv_copy` already takes the destination pointer, so it
is a small step, but it saves one 4-to-32-byte copy per message *while a
receiver is parked*, which is not where the time is. Rust's remaining lead
(2.3 ms against 2.7 ms) is its std channel's lock-free array ring (crossbeam,
after Vyukov's bounded MPMC queue). That is CHANNELS_PLAN Phase 4, and it is the
next thing to measure against, not this.

## Reproduce

```bash
python3 benchmarks/run.py --compiler .prismio/build/debug/pc --only channel_pipeline --runs 21 --output /tmp/r
```

Tests: `tests/test_232_channel_copies.psm` (checksums, send after close, close
with a blocked receiver, an owned message staying boxed, a received value in a
`Vec`, one kept across iterations); the `channel_copies` harness check reads its
IR and requires clean `--verify` ledgers for it and test_96.
