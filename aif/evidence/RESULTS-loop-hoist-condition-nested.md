# quicksort and graph_bfs: what the gap was, 2026-10-01

Alternating runs, 41-301 per row, one binary per arm, checksums identical.

## quicksort: 1.12x -> 1.02-1.03x of C++

`while (values[i] < pivot) { i = i + 1 }` reads only in its **condition**.
`generateLoopFlatGuard` looked for a receiver to hoist (`irCaptureStableListBound`)
in the loop *body* alone, and `generateWhile` cleared the enclosing loop's hoisted
`data`/`len` on entry. So every scan reloaded `data` per element, and because the
data load sat behind the in-range branch, LICM could not lift it.

Two changes, both in `src/ir/`:

- `irCaptureStableListBound` takes the condition too: it is a place to find a
  receiver, and a push in it ends the receiver's stability as much as one in the body.
- `generateWhile` no longer clears the enclosing loop's hoisted values. The
  enclosing capture already required that nothing in its whole body, nested loops
  included, rebinds or pushes the list.

C model (`clang -O3`, real `RtList` layout, 100k Ints, min of 41): total-semantics
as emitted 1.12-1.14x, `data`/`len` hoisted 1.03-1.04x, speculative check that
bails to the generic loop 1.04-1.05x, no checks 1.00x. Hoisting alone is enough;
the bail design buys nothing more and needs new machinery.

Suite: 504/504, `tools/aif_differential.py` agrees on 19 sources. 55-benchmark
A/B before/after: nothing outside noise regressed; quicksort -8%, mergesort -3%.
`gcd_lcm` read +5% in one build and its machine code is byte-identical to the
other build apart from three trailing `nop`s -- placement, not code.

What is left is not code: in-process after warm-up Prismio is 3.82-4.15 ms and C++
3.81-3.97 ms; across processes Prismio's sort phase spreads 3.97-4.33 ms where
C++ spreads 3.92-4.10 ms. Replacing `benchSwap`'s two reads and two writes with
`values.swap(a, b)` measured 1.037x -> 1.033x and was reverted.

## graph_bfs: not a code gap

C++ with `width` a compile-time 480: 576 us. Prismio: 575-578 us. The C++ arm ran
at 531 us only because `scale` crossed a translation-unit boundary, so it divided
by a run-time value with hardware `sdiv`. On Apple silicon `sdiv` beat the
multiply-shift sequence by 8% in this one loop (two divisions by different
constants plus the checksum recurrence, throughput-bound).

It does **not** generalise. Forcing `sdiv` (opaque divisor) in C, min of 15:

| case | multiply-shift | sdiv |
|---|---:|---:|
| dependent `% 1000000007` | 9.5 ms | 11.7 |
| gather `% 480` | 2.5 | 2.6 |
| digit loop `/ 10`, `% 10` | 0.95 | 1.53 |
| vectorisable `% 480` | 0.53 | 1.89 |

So constant division is left as LLVM lowers it. The benchmark now builds the C++ arm
with `-flto` and the Rust arm with `-C lto=fat -C codegen-units=1`, because the
Prismio arm is always whole-program; graph_bfs reads 1.00x of both.

Also seen and *not* a bug: with two multiply-high divisions in one loop, LLVM
AArch64 (and clang on plain C) lowers the other one as `lsr x,#32; asr w,#28`
instead of a single `asr x,#60`. Forcing the fused form by hand measured 10% slower.

## mandelbrot: 1.12x -> 0.99x of C++ (and Rust is 1.25x)

Every float op already carried `contract`, but the multiply in `x*x + y*y` and the one
in `x*x - y*y` are one value by the time instruction selection sees them (LLVM merges the
two), and a multiply with two users is fused into neither add: a standalone `fmul`, then
`fsub`/`fadd`, where clang emits `fnmsub` and `fmadd`. That lengthens the `x` chain
(multiply 4 + subtract 3 + add 3 against fused 4 + add 3). Clang decides at the source
expression, so there is nothing to merge. `ir_fadd`/`ir_fsub` now do the same
(`llvm.fmuladd`, left operand's multiply first, only a multiply nothing has used yet).
Same instruction sequence as clang's. Suite 504/504; every benchmark still returns the
same answer as C++ and Rust.

## edit_distance: not a code gap

Bimodal in *every* language: ~560 us or ~700 us per run, same per mode, and the share of
runs in each differs (Prismio ~50% slow, C++ ~35%). Best runs are equal.

## The verdict rule (benchmarks/run.py `verdict`, schema 3)

A flat 4% (terminal) and 5% (HTML hero) were applied to 0.6 ms runs whose process-to-
process jitter is 10-25%, and the HTML's median-and-MAD noise estimate reads a bimodal
run as 0% noise, so `edit_distance` was shown as a 1.18x loss. A result is now a win or a
loss only when *both* the ratio of medians and the ratio of best runs leave a tolerance:
medians `max(0.04, either arm's IQR/median, 25 us/median)`, best runs
`max(0.04, 25 us/min)`. Recorded per workload in the JSON; terminal and HTML both read it.

## large_buffer_copy: still 1.14-1.16x, and why

C++ and Rust turn the eight identical `target[i] = source[i]` rounds into one `memcpy`
(loop idiom, full unroll, then dead-store elimination of the identical repeats). That
last step needs LLVM to know `source` and `target` are different allocations, which
`std::vector` gets from two `noalias` `operator new` results.

Tried and measured, both nothing, both reverted:

- **Per-binding scoped-noalias for element accesses** (a fresh, never-rebound local
  `Vec` owns its block; key = binding name; scopes in a domain per function). Correct in
  the IR, sound by construction, **no measurable effect on any of 55 benchmarks**
  (all rows within noise of the build without it).
- **`for` loop block copy** (MEM-006 for `for i in a..<b`), `memcpy` when both lists are
  keyed distinct. The `memcpy`s are emitted but all eight survive: DSE cannot delete the
  earlier ones unless the second copy's *read* of `source` is shown not to overlap the
  first copy's *write* to `target`, and scoped-noalias is per instruction, so a `memcpy`
  cannot say "my source and destination differ" without also claiming it does not read
  its source.

What would work is `noalias` on the two *pointers*, which LLVM only takes on function
parameters (Rust's `&mut`) -- the 2014 proposal to look through loads tagged with
metadata was never merged. Outlining the copy into an internal function with `noalias`
pointer parameters does not obviously help the repeats, which are separate inlined
instances. Open.
