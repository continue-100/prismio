# Binary size and compile time against C++ and Rust (2026-09-28)

Three backend changes and one language addition, measured on an M-series Mac
(4 performance + 6 efficiency cores), LLVM 23.1.1, against the benchmark suite's
C++ (`clang++ -O3`, seven TUs) and Rust (`rustc -C opt-level=3`, one crate) arms.

## Where it stood

| | Prismio | C++ | Rust |
|---|---:|---:|---:|
| benchmark suite binary | 558,688 B | 161,864 B | 705,800 B |
| benchmark suite compile | 1.98 s | 2.15 s | 0.73 s |
| hello world binary | 52,040 B | 33,432 B | 465,608 B |
| hello world compile | 64 ms | 120 ms (`puts`), 188 ms (`iostream`) | 60 ms |

The suite binary carried 136 `str*` std functions it never called and a 79 KB
`__TEXT,__const` that was the Unicode case tables those functions reach. Every
function the program module defined was external, so nothing removed them: they
were optimised at -O3, code-generated and kept by ld64.

The suite's 2.2 s build was 0.11 s frontend, 0.07 s library merge, 0.04 s
re-parse, **1.89 s of `default<O3>` plus machine code on one thread**, 0.1 s link.

## What changed

1. **Internalisation** (`internalize_executable`, runtime/llvm-api-backend.c). A
   closed executable -- no native sources, linked objects or `exportDynamic`
   (`program_is_closed`, build_driver.c) -- makes everything but `main` internal
   and runs `globaldce` before the pipeline.
2. **Parallel machine code** (`emit_partitioned`). The whole program is
   optimised as one module, then split into up to eight partitions lowered on
   their own threads, each in its own `LLVMContext`, from one bitcode image --
   LLVM's LTO split. No inlining or IPO decision is made per partition.
3. **`-dead_strip`** on every Mach-O link.
4. **`cold fn`**, a contextual modifier lowering to LLVM `cold` + `noinline`,
   and `PRISMIO_NOINLINE` on the runtime's remaining fast/slow splits. Needed by
   (1); see below.

## Where it stands

| | Prismio | C++ | Rust |
|---|---:|---:|---:|
| benchmark suite binary | **241,376 B** (0.43x of before) | 161,864 B | 705,800 B |
| benchmark suite compile | **0.95-1.03 s** | 2.15 s | 0.73 s |
| hello world binary | **33,960 B** | 33,432 B | 465,608 B |
| hello world compile | **56 ms** | 120-188 ms | 60 ms |
| compiler self-build, machine code | **0.66 s** (was 2.14 s) | | |

Suite stages now: merge 70 ms, re-parse 43 ms, IR pipeline 575 ms, machine code
120 ms in 8 partitions (430 ms whole). C++ links `libc++` dynamically and Rust
links its std statically, which is most of the three-way size difference; the
suite's remaining text is the benchmark code itself at -O3, inlined and
vectorised, which is performance this suite exists to keep. The runtime's share
is 11 KB.

Runtime performance, `prismio bench` at HEAD against this tree: geomean vs C++
0.879 -> **0.839**, vs Rust 0.791 -> **0.753**. Alternating A/B of the two suite
binaries (9 runs, one process per run): geomean **0.978** over 62 workloads.

## Internal linkage changes inlining, both ways

LLVM inlines an internal function's **only** call whatever its size. That is the
wins -- string_search 0.57x (`strTwoWayIndexOfFrom` and `str_find_needle`
inlined and specialised on the constant needle), string_join 0.73x, gcd_lcm
0.84x, binary_search 0.86x, tokenization 0.91x, hashmap_insert_lookup 0.92x --
and it undoes every slow path split out on purpose so its fast half can inline:

- `mapInsert` went back into `mapSet`, which grew from 52 to 154 instructions and
  stopped inlining into the caller's loop: key_value_update **1.28x**.
- `list_set` went into `list_set_inline_scalar`, which then stopped inlining into
  a sort's swap: quicksort **1.13x**.

Tried first and rejected: a "split" mode that internalised, ran `globaldce`, then
restored the survivors to external linkage for the pipeline. It reproduced the
old inlining exactly (geomean 0.991, one regression) and gave up every win above
(geomean 0.985 for full internalisation before the fixes). What the splits
needed was a way to say "this half is cold", which the language did not have.
`cold fn mapInsert` took key_value_update to 0.97x; an out-of-line
`list_set_unstamped` took quicksort to 0.99x.

## Residuals, measured and not fixed

- **indirect_calls 1.08x** of the old compiler (C++ parity, 1.07x of Rust).
  Internal linkage lets IPSCCP prove `benchIndirectMix`'s argument is in
  [0, 1000); LLVM narrows `% 1009` to 16 bits, and AArch64's 16-bit
  division-by-constant sequence is longer than the 32-bit one. An LLVM codegen
  quirk; nothing in the program is wrong.
- **graph_bfs 1.06x**, steady across runs, code changed in branch arrangement
  only; absent in the split mode, so it is internal linkage's.
- **flat_bitset** reads 1.03-1.10x run to run; its fallback call sites never
  execute (lldb hit count 0). Treat as layout until a per-symbol diff says
  otherwise.

## A bug worth remembering

The first parallel emitter corrupted IR randomly -- PHIs, attributes, missing
terminators -- in 9-15 of 20 builds, never with one thread, and a standalone
harness against the same LLVM archives was clean. The cause was ours:
`delete_function_body` deleted each block right after emptying it, while a branch
in a later block still pointed at it. Release LLVM does not assert on it; erasing
that branch later wrote into the freed block's use list. With one thread the
memory was rarely reused in time; with eight, another partition's IR was
allocated there. Erase every instruction first, then delete the blocks: 0 of 30,
then three self-hosted generations.

## Second round

- **The merged module stays in memory.** Printing it to `libraries-<pid>.ll` and
  parsing it back was 70 ms of the suite's build (merge 70 -> 48 ms, re-parse
  43 -> 0). Suite build ~0.95 s -> **~0.85 s**.
- **`exportDynamic` exports the native objects' symbols, not everything.** The
  compiler exported 48,747 symbols, ~44,000 of them LLVM C++; now 901, and
  `-dead_strip` can drop the LLVM code nothing calls: **135.8 MB -> 125.2 MB**.
  `run --jit` unchanged (suite's `jit` fixture).
- **`cold fn listHeapSort`**, pdqsort's adversarial-input fallback: it was inlined
  into every sort instantiation, the two slowest functions in the suite to
  optimise. IR pipeline 575 -> 540 ms; sort_strings, quicksort, mergesort and
  word_frequency within 1%.

Measured and not pursued:

- A site-to-key and site-to-owned transpose in AIF bracketing
  (`bracket_site_bounded`). IR byte-identical, and no change in time: the
  frontend's AIF cost is spread over a dozen functions at 50-100 ms each on the
  compiler's own source, with no single hotspot left. Reverted.
- Re-optimising the runtime's C functions is ~35 ms (7%) of the suite's
  pipeline; not worth special-casing.
- Writing the merged module as bitcode instead of text: 70 -> 74 ms merge,
  43 -> 47 ms parse. Slower; the in-memory handoff replaced both.
- 37 MB or more of the compiler is LLVM backends Prismio does not document
  (KNOWN_ISSUES); a product decision, not taken here.

## Verification

- `tools/run_suite.py`: 469/469.
- IR of all 266 buildable programs in `tests/`, `aif/corpus/` and `benchmarks/`
  against the pre-change compiler, from a tree without `runtime/`: identical but
  for `cold noinline` on `mapInsert`, `map.plib` panic lines moved by the five
  comment lines above it, and the toolchain path in panic strings.
- Seed refreshed; `tools/bootstrap.sh --seed` then one generation from it builds.
- `tools/aif_differential.py`: engine and oracle agree on all 19 sources.
- Both doc example gates: 256 and 50 snippets.
- IntelliJ plugin tests, including the corpus lex of this checkout.
- Parallel codegen under `PRISMIO_CODEGEN_VERIFY=1`: 0/30 and 0/20 on the suite.
