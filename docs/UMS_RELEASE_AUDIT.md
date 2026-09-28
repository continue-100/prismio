# UMS release audit

2026-09-28. Scope: `ums/`, `src/project/ums_cli.psm`, the CLI dispatch in
`src/main.psm`, the C helpers they call (`runtime/build_driver.c`,
`runtime/program_support.c`), the repository's own `build.ums` commands and the
Python tools behind them, and the user docs that describe all of it
(`../website/apps/docs/content/package-manager/index.md`).

The question asked: is this ready to ship to general users?

**Not yet.** The overall design is sound: the stable `toolchain` prefix, the ABI
handshake, staged host promotion, stable `UMS`/`P` diagnostic codes, and the
token-preserving manifest writer. What blocks the release is the layer where UMS
touches the operating system: how steps are started, where they run, which
binaries run, and what exit status comes back.

**How this was checked.** Every finding marked *reproduced* was run against a
renamed copy of the project host (`.prismio/build/debug/prismio`, built
2026-09-27 17:14) in a scratch toolchain, from projects created with
`prismio init`. The copy was renamed so the launcher would not forward (the launcher routes by
basename). Findings marked *code-read* were not run, and the
Windows ones in particular need a Windows host to confirm.

## Resolution (2026-09-28, same day)

Every item below was fixed in the working tree except where this section says
otherwise. What changed shape rather than just behaviour:

- **Nothing about the compiler is built into the toolchain.** `component(
  "prismio.backend")`, the `prismio bootstrap` verb, the backend half of
  `prismio_toolchain_files[]` and the packaged `lib/backend.a` are gone. A
  target declares its own C: `native { source include define flag
  responseFile }`, `runtime = "installed" | "none"`, `exportDynamic = true`, and
  `link { responseFile(...) }`. The compiler's own `build.ums` uses exactly
  those, with LLVM from `third_party/llvm-{compile,link}.rsp`, which
  `tools/setup_llvm.py` now writes. The manifest-built compiler emits IR
  byte-identical to the bootstrap-built one (asserted in `run_ums_test`).
- **Every program the driver starts goes through one argv spawn**
  (`compiler_spawn_wait`, runtime/build_driver.c) with a working directory and
  the child's real exit status: `run` (and `run --jit`), `test`, every command
  step, the host forward and the probes. `command_quote_arg` quotes correctly
  for each shell too, for the clang lines that still use one.
- **Project hosts are trusted by identity** (`<host>.trusted`, written on
  promotion), and must live under `.prismio/`.
- **Profiles are real**: `debug` = `-g` + overflow checks, `release` = `-O3`,
  both overridable in a `profiles` block. The compiler's manifest turns both off
  for its debug profile.
- `src/project/ums_cli.psm` split into `ums_cli.psm` (verbs), `host.psm`
  (routing, trust, promotion) and `commands.psm` (project commands);
  `compileSource` takes a `CompileOptions` struct.

Found and fixed on the way, outside the audit's list:

- **Function names of 128+ bytes were truncated at their definition only**
  (`NAME_LEN` in llvm-api-backend.c), so the call and the definition were
  different symbols. Function names now have a 1024-byte buffer, and a name that
  would not fit a fixed buffer is a backend error instead of a silent rename.
- **`--overflow-checks` trapped inside the standard library** (`keyMixWide`
  wraps on purpose). The check now never applies to std code.
- **`run --jit` could not run a program using `std.map`** from an installed
  toolchain: the JIT skipped the `.plib` merge a build does.
- A `std/` directory in any ancestor shadowed the installed library file by
  file; only a Prismio checkout's `std/` does now, which is what the user docs
  already claimed.

Not fixed: the Windows paths (`_spawnv` replacement, `py -3`, the trust stamp's
file index, `windows_export_flags` over native objects) are written and not run
-- there is no Windows host here, and CI's Windows leg is their first
execution.

## P0 — must fix before a user release

### 1. Command-step arguments are interpreted by the shell *(reproduced)*

`command_quote_arg` (`runtime/program_support.c:491`) wraps an argument in `"`
and escapes only `"`. On POSIX, `$`, backticks and `\` are still live inside
double quotes, and the line goes to `system()`.

```text
commands { command("sh") { shell("echo", args) } }

$ prismio sh '$(whoami)'
vibrant                         <- the substitution ran
$ prismio echo 'trail\'
sh: -c: line 0: unexpected EOF while looking for matching `"'
```

The README and the user docs promise the opposite: "Every argument of every step
is quoted for the platform's shell, so an argument containing spaces or
metacharacters stays one argument". On Windows the same function is wrong in a
different way: `%VAR%` expands inside quotes, and `\"` follows the CRT's rules
rather than cmd's.

**Fix.** Stop building a shell line. `program_support.c` already has the argv
spawn that `std.process` uses (`proc_spawn_*`). Start `run` and `shell` steps
with it, and do the same for `compiler_run_executable_with` and
`compiler_probe_executable`. `shell(...)` names a program plus its arguments, so
it does not need a shell either. `command_quote_arg` can then stay a
build-driver-only helper for clang lines, where every input is a path the
compiler chose itself.

### 2. `toolchain.host` executes a committed binary on every command *(reproduced)*

`dispatchToUmsHost` runs before any verb is parsed. If a project's first block
names a host that exists, the global `prismio` does three things with it: runs
it with `--version`, runs it with `--internal-host-abi`, and then forwards the
user's command to it. With `host = "bin/tool"` pointing at a shell script
committed to the repository, the script ran for `prismio --version` and for
`prismio check src/main.psm`. The IntelliJ plugin runs `check` whenever a file
is opened, so opening a cloned repository in the IDE is enough to execute
whatever it ships.

The handshake is not a defence, because it only checks the exit status: a
script that exits 0 passes it. Lowering rejects absolute host paths, but
`../`-relative paths are accepted, and `umsProjectHost` (the prefix reader the
launcher actually uses) does not validate the path at all.

**Fix.** Only honour a host this machine built. The launcher already owns
promotion, so it can record the promoted binary's SHA-256 in
`.prismio/host.stamp`, and route only when the file at `toolchain.host` matches
that stamp. `.prismio/` is ignored by git, so a clone never carries a stamp and
falls back to stage 0, which then offers `prismio build` to create a host.
Also require `toolchain.host` to resolve inside `.prismio/`.

### 3. `run` cannot pass arguments, and a program's exit status is lost *(reproduced)*

```text
$ prismio run -- a b          error[P1019]: unknown argument `--`
$ prismio run a b             error[P1050]: unknown argument `b`, then ~60 lines of usage
$ prismio run src/main.psm hi error[P1050]: unknown argument `hi`
```

A program that returns 3 is reported as a compiler error
(`error[P1023]: … exited with a failure status`), and `prismio` itself exits 1.
Every layer between the program and the user collapses the status to 0/1:
`execute_command`, `compiler_run_executable_with`, and `compiler_forward_cli`.
Project commands behave the same way: a step that exits 7 becomes exit 1 plus a
`P1059`.

**Fix.** Support `prismio run [--release] [-- args...]` and
`prismio run file.psm [flags] [-- args...]`. Pass the program's own exit status
through unchanged, and report nothing extra when the program itself returned
non-zero. Propagate step and hosted exit codes the same way. A diagnostic is for
the case where the toolchain failed, not the program.

### 4. `--release` changes the directory and nothing else *(reproduced)*

`cmp .prismio/build/debug/hello .prismio/build/release/hello` reports the two
files identical. Both profiles call `compileSource` with the same flags: whole
program at `-O3`, no `-g`, no `--overflow-checks`. So the debug profile has no
debug info, and users get no signal about which profile they need.

**Fix (a decision for you).** One option: debug = `-g` plus
`--overflow-checks`, release = `-O3` as today. The other: keep one profile and
remove `--release` before 0.1 promises it. Performance is the project's goal,
which argues for release staying exactly as it is. The problem is only that
debug is currently the same thing under another name.

### 5. Command steps run in the invoker's directory, not the project root *(reproduced)*

`build.ums` is found by walking upward, and `run` subjects are resolved against
the root. But the process runs with whatever working directory the user had.
Run from `src/`, a step printed `cwd: …/edge/src`. Every relative argument in a
manifest is therefore wrong from a subdirectory. That includes this
repository's own `--compiler .prismio/build/debug/prismio` and `--out dist/…`:
`release.py` resolves both against the caller's directory.

**Fix.** Start each step with the working directory set to the project root.
The argv spawn from item 1 takes a directory, so this comes almost free with
that fix.

## P1 — correctness and robustness

| # | Finding | Evidence | Fix |
|---|---|---|---|
| 6 | A `run("x/e.psm")` tool is built at `.prismio/build/<profile>/e`, the same path as target `e`, and overwrites it. A `tools/prismio.psm` in this repository would overwrite the project host. | reproduced | Build tools into `.prismio/build/<profile>/tools/`. |
| 7 | `umsValidName` accepts `.`, `..` and a leading `-`. `executable("..")` passes validation and fails at link with `open() failed, errno=21 (Is a directory)`. | reproduced | Require a leading letter or digit; reject `.` and `..`. |
| 8 | On Windows, the repository's `dist`, `ship` and `verify` pass `.prismio/build/debug/prismio` and `dist/Prismio/bin/prismio` without `.exe`. `package.py` and `release.py` check `is_file()` and stop with "no compiler at". CI never runs a manifest command, so nothing notices. | code-read | One helper in `tools/` that appends `.exe` when the extension-less file is missing. Add one CI step that runs `prismio dist` through the manifest. |
| 9 | `compiler_forward_cli` uses `_spawnv` on Windows. That call joins arguments with spaces and does no quoting, so an argument containing a space is split on its way to the host. This contradicts the comment above the function. | code-read | Build a quoted command line with the CRT rules and call `CreateProcessW`, or reuse the item 1 spawn. |
| 10 | `verify` runs `run_suite.py`, which tests the project host, but then runs `check_externs` and `aif_differential` against `dist/Prismio`. Nothing in the command builds `dist` first, so one gate can check two different compilers, one of them stale. `lists` has the same unstated precondition. | code-read | Make `dist` the first step of both commands, or point every step at the host. |
| 11 | The lockfile is written to `.prismio/prismio.lock`, which `init` gitignores. It records absolute paths, including the manifest's own path. The docs say "Check it in: it exists to be reviewed." | reproduced | Write `prismio.lock` at the root with root-relative paths, or stop telling users to commit it. |
| 12 | SemVer validation is wrong in both directions: `1.0.0-beta.1` (valid SemVer) is rejected with "must use semantic version form", and `01.02.0003.4` is accepted. | reproduced | Implement the SemVer 2.0 grammar: exactly three components, no leading zeros, optional `-pre` and `+build`. |
| 13 | `prismio = "99.0"` is accepted. The declared compiler version is never compared with the running compiler. | reproduced | Error when the declared major.minor is newer than `PRISMIO_VERSION`. |
| 14 | Every link failure appends "If you are building the Prismio compiler itself, use `prismio bootstrap`". A user whose `library("sqlite3")` is missing gets that advice. | reproduced | Print the note only when the undefined symbols are `ir_*` or `LLVM*`. |
| 15 | `component("prismio.backend")` validates in any project. Outside a checkout it fails at build time with a raw C `ERROR: bootstrap needs the Prismio repository sources`. | reproduced | Make it a UMS validation error unless the manifest root holds `runtime/lang_runtime.c` (see the earlier note on the component's name). |
| 16 | `clean` removes planned target outputs only. A `.psm` tool binary survived `clean`, and so do the host's `lib/` and `stdlib/`. `runUmsScriptStep`'s comment says "`clean` owns that directory". | reproduced | Clean the profile directory recursively; that needs a `remove_tree` primitive. |
| 17 | `prismio build e`, where `e` is a target name, reports `error[P1008]: cannot read e`. | reproduced | If the bare word names a declared target, build that target; otherwise list the declared targets in the error. |

## P2 — user experience and consistency

- **The reserved-name list exists in four places.** `umsReservedCommandName`,
  the `main()` dispatch, the `P1039` note, and the docs. None of them covers
  `--internal-host-abi` or a name ending in `.psm`, both of which dispatch
  before project commands. Keep one table in `main.psm` and derive the other
  three from it.
- **Help is written for compiler developers.** `--help` lists `bootstrap`,
  `runtime-hash`, `dump-ast`, `--force-layout`, `--theta-fields` and
  `--copyable-collections` alongside `init` and `run`. Every unknown-argument
  error then prints about 60 lines of that. `--help` inside a project does not
  list the project's own commands; they appear only after a typo. Suggested
  split: a user `--help`, a `--help-all` for developers, and a one-line
  "see `prismio --help`" on argument errors.
- **Tests.** A compile error in one test aborts the whole run, and there is no
  `prismio test <name>` filter.
- **Most validation diagnostics carry no location.** Errors like `UMS2304` and
  `UMS23xx` print `build.ums: error[…]` with line 0, even though the lowered
  statement knows its line. Duplicate top-level blocks (`UMS2007` through
  `UMS2013`) have the same problem.
- **`UMS2504` means two things:** an unknown step and an unknown command
  property.
- **Any ancestor directory's `std/<leaf>.psm` shadows the installed stdlib,
  file by file, up to 64 levels up** (`standardModulePath`). This is documented,
  and it is what makes a checkout build against its own `std/`. But a user
  project that has its own `std/io.psm` gets that one file from itself and every
  other module from the install. Limit the ancestor search to a directory that
  also contains `runtime/lang_runtime.c`, meaning a real checkout.
- **Dependencies are recorded but never used.** Path dependencies are not added
  to import search. The user docs say so, but a manifest that declares one gets
  no warning.

## P3 — minor

- A forwarded hosted command leaves `PRISMIO_INTERNAL_HOSTED=1` in the
  environment of every program it runs, so a nested `prismio` launcher inside
  that program will not route.
- `.py` steps run `python3`, or `python` on Windows. There, `python` can be the
  Microsoft Store stub. Falling back to `py -3` would be more robust.
- `UmsLexer.slice` builds strings one character at a time, which is quadratic.
  It is harmless at manifest sizes.
- The `suite` comment block in `build.ums` makes the same point twice in two
  paragraphs.

## The repository's own commands

| Command | macOS/Linux from the root | From a subdirectory | Windows |
|---|---|---|---|
| `dist` | works | fails: relative `--compiler`/`--out` (item 5) | fails: no `.exe` (item 8) |
| `ship` | works | fails (item 5) | fails (item 8) |
| `suite` | 282/283 by design (`KNOWN_ISSUES.md`) | works: `run_suite.py` anchors on the repository | works |
| `bench` | works | fails (item 5) | likely works: `CreateProcess` appends `.exe` |
| `lists` | needs an existing `dist/` (item 10) | fails (item 5) | fails (item 8) |
| `verify` | two compilers in one gate (item 10) | fails (item 5) | fails (items 8, 10) |

## Suggested order

1–3 and 5 share one change: steps and `run` start processes through the argv
spawn with a working directory and pass back the real exit status. Item 2 (host
stamp) is separate and small. Item 4 needs your decision first. After that come
6, 7, 11 and 13, which are UMS-only changes with fixtures, then the Windows
items once there is a host to test them on.

Changes to `src/` and `runtime/` go through the usual path: a two-generation
fixpoint, the full suite, `tools/aif_differential.py`, and a seed refresh where
new syntax is involved (none of the fixes above need one). Update the website
docs in the same change for 1, 3, 4, 5 and 11.
