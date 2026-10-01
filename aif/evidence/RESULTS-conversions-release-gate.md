# Conversions: the release gate, run on a packaged RC

**`build/cv-rc3`**, packaged from `build/cv-g1` (bootstrapped off `build/cv-n2` at
`1287d89` plus a trailing-newline edit in `src/lexer/scanner.psm`). Gate green:
two-generation byte-identical fixpoint, suite 492/492, differential 19/19,
7 corpus programs built and run, `--verify` 0 leaked / 0 violations.

```bash
bash tools/bootstrap.sh --compiler build/cv-n2 --out build/cv-g1
python3 tools/package.py --compiler build/cv-g1 --out build/cv-rc3 \
    --target x86_64-apple-macos --sysroot x86_64-apple-macos=$(xcrun --show-sdk-path)
PATH=$PWD/third_party/llvm/bin:$PATH python3 tools/release_gate.py --rc build/cv-rc3/bin/prismio
```

```
source lists agree                         ok
two-generation bootstrap                   ok
compiler IR fixpoint                       ok    byte-identical
RC reproduces itself                       ok    the frozen binary emits generation 1's IR
seed agreement                             ok    committed seed builds the compiler
full suite                                 ok    492/492
AIF oracle differential                    ok    agree on all 19 sources
corpus builds and runs                     ok    7 programs
--verify sweep                             ok    0 leaked / 0 violations on every program
curated runtime off                        ok
object cache off                           ok
JIT                                        ok
cross-target                               ok    x86_64-apple-macos built
packaged toolchain                         ok    all separation checks passed
```

## Two defects in the gate's own harness

Neither was a compiler defect, and the first read as one.

- **The RC was not the compiler under test.** Packaged, it is `bin/prismio`, and a
  compiler of that name run inside the checkout is the launcher: it forwards to
  the project host. Every step measured the host, and passed only while the host
  happened to be built from the same tree. Cross-target exposed it: the host's
  toolchain has no x86_64 runtime. The gate now runs a copy beside the original
  under another name (`under_neutral_name`, as `aif_differential.py` does) and
  reports the original path.
- **`target_cross` ran what it had just built for another CPU.** Step 7 builds an
  x86_64 binary on arm64 macOS and executes it, assuming Rosetta. Without it
  `exec` fails with `Bad CPU type in executable` and the whole test died on an
  uncaught `OSError`, which is the one failure of 492. The build and the `file`
  check already judge the cross build; only the *run* needs Rosetta, so an
  `OSError` there now reports `built, not run here` instead. A host that can run
  x86_64 is unchanged: it still runs the binary and checks its output.

## Not covered

- **x86_64 binaries were built, not run** (no Rosetta here).
- **No Windows or Linux run.**
- **No `--old` argument**, so the per-function mnemonic diff against a previous
  compiler was not part of this run.
- **The corpus is 7 programs, not the 30 the v0.1 record names.** `aif/corpus/`
  holds eight sources and the gate skips `g6_engine`; nothing in this work
  touched it.
