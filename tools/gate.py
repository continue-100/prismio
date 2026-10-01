#!/usr/bin/env python3
"""The pre-push gate, in one command: what CI checks that can run on this machine.

    prismio gate
    python tools/gate.py --compiler .prismio/build/debug/prismio

Three steps, stopping at the first that fails:

  1. `tools/lint.py`, which CI runs before anything is built.
  2. Packaging the compiler the way RELEASE.md says -- a *packaged* compiler,
     because a bare generation has no `lib/runtime/*.bc` and fails every program
     the suite builds. On macOS the package also carries `x86_64-apple-macos`
     and the SDK sysroot it needs, because the gate's cross-target check builds
     for it and a package without that runtime fails the check for a reason that
     has nothing to do with the change being tested.
  3. `tools/release_gate.py` on that package, with the pinned LLVM first on PATH:
     the system's `clang` and `llvm-nm` cannot read LLVM 23 bitcode, which fails
     the packaged-toolchain check, `module_artifacts` and `target_cross`.

It does not run what only another platform or a CI runner can: Windows, the
Linux-only sanitizer smoke, the benchmark smoke, and the smoke program inlined in
`.github/workflows/ci.yml`. A green run here is the strongest local statement
short of a CI run, not a replacement for one.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXE = ".exe" if os.name == "nt" else ""


def pinned_llvm_bin() -> str:
    paths = REPO / "third_party" / "llvm-paths.json"
    if not paths.is_file():
        return ""
    return json.loads(paths.read_text(encoding="utf-8")).get("bin", "")


def macos_cross_flags() -> list:
    """`--target`/`--sysroot` for the gate's cross-target check, or nothing."""
    if sys.platform != "darwin" or not shutil.which("xcrun"):
        return []
    probe = subprocess.run(["xcrun", "--show-sdk-path"], capture_output=True, text=True)
    sdk = probe.stdout.strip() if probe.returncode == 0 else ""
    if not sdk:
        return []
    return ["--target", "x86_64-apple-macos", "--sysroot", f"x86_64-apple-macos={sdk}"]


def step(label: str, command: list, env: dict) -> int:
    print(f"\n=== {label}", flush=True)
    status = subprocess.run([str(c) for c in command], cwd=str(REPO), env=env).returncode
    if status != 0:
        print(f"\nGATE FAILED at: {label}", flush=True)
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint, package, and run the release gate.")
    parser.add_argument("--compiler", required=True,
                        help="the compiler to package, e.g. .prismio/build/debug/prismio")
    parser.add_argument("--out", default="build/gate-rc",
                        help="where the candidate is packaged (default: build/gate-rc)")
    args = parser.parse_args()

    env = dict(os.environ)
    llvm = pinned_llvm_bin()
    if llvm:
        env["PATH"] = llvm + os.pathsep + env.get("PATH", "")

    out = Path(args.out)
    if not out.is_absolute():
        out = REPO / out
    if out.exists():
        shutil.rmtree(out)

    steps = [
        ("lint", [sys.executable, "tools/lint.py"]),
        ("package the candidate", [sys.executable, "tools/package.py", "--compiler",
                                   args.compiler, "--out", out, *macos_cross_flags()]),
        ("release gate", [sys.executable, "tools/release_gate.py", "--rc",
                          out / "bin" / f"prismio{EXE}"]),
    ]
    for label, command in steps:
        status = step(label, command, env)
        if status != 0:
            return status
    print("\nGATE PASSED -- safe to push as far as this machine can tell.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
