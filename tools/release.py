#!/usr/bin/env python3
"""Build the distributable artifacts for a release, and their checksums.

    python tools/release.py --build-with .prismio/build/debug/prismio --out dist/release
    python tools/release.py --compiler build/v0.1-rc --version 0.1.0 --out dist/release

**`--build-with` ships this checkout, not a binary that happens to be lying
around.** It runs `<compiler> build --release`, and what it ships is that
build's `.prismio/build/release/prismio`, compiled from the tree as it is now.
`prismio release` does this. Shipping the project host directly, as it used to,
packaged whatever the last `prismio build` left: an edit that does not change
the compiler's own IR -- a runtime fix, a link flag -- passed the fixpoint check
and shipped the old binary. The runtime bitcode and the standard library never
had that problem: tools/package.py rebuilds both from source every time.

`--compiler` ships the binary it names, as it is: a frozen release candidate
that has been through the gate (RELEASE.md §1).

One archive per host, named for the triple it was built on, plus a SHA-256
manifest covering it. Run it on each platform; the manifests concatenate, which
is what lets three machines produce one checksum file without any of them
trusting the others.

**It refuses to build from a compiler that is not a fixpoint.** A release
artifact whose compiler does not reproduce its own IR is a compiler caught
mid-migration, and that is the one defect this project has burned commits on.

**It reads the oldest system the artifact runs on off the binaries**, because
nothing else notices: the 0.1.0 macOS archive said `minos 27.0`, the build
machine's version, and would not start on macOS 26 (2026-10-02). See
`check_floor` for what each platform is held to.

The archive is `.zip` on Windows and `.tar.gz` elsewhere -- the format each
platform can open without installing anything.
"""
import argparse
import filecmp
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from executable import resolve_executable

REPO = Path(__file__).resolve().parent.parent
WINDOWS = os.name == "nt"
EXE = ".exe" if WINDOWS else ""


def die(message: str, hint: str = "") -> "NoReturn":
    print(f"error: {message}", file=sys.stderr)
    if hint:
        print(f"       {hint}", file=sys.stderr)
    raise SystemExit(1)


def run(command: list, **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run([str(c) for c in command], capture_output=True, text=True,
                          cwd=str(REPO), **kwargs)


def host_triple() -> str:
    machine = platform.machine()
    system = platform.system()
    if system == "Darwin":
        return f"{machine}-apple-darwin"
    if system == "Linux":
        return f"{machine}-unknown-linux-gnu"
    if system == "Windows":
        return f"{machine}-pc-windows-msvc"
    return system.lower()


def reported_version(compiler: Path) -> str:
    """The version the compiler reports is the version that ships. Taking it from
    a flag alone would let an archive be named for a number the binary inside it
    does not say, which is the kind of mismatch nobody checks until a bug
    report."""
    result = run([compiler, "--version"])
    if result.returncode != 0 or not result.stdout.strip():
        die("could not read the compiler's version")
    first = result.stdout.strip().splitlines()[0].split()
    if len(first) < 2:
        die(f"unexpected --version output: {result.stdout.strip().splitlines()[0]}")
    return first[1]


def llvm_objdump() -> Path:
    info = json.loads((REPO / "third_party" / "llvm-paths.json").read_text())
    return Path(info["bin"]) / f"llvm-objdump{EXE}"


def macos_minos(binary: Path) -> str:
    r = run([llvm_objdump(), "--macho", "--private-headers", binary])
    for line in r.stdout.splitlines():
        words = line.split()
        if len(words) == 2 and words[0] == "minos":
            return words[1]
    die(f"{binary.name} states no minimum macOS (no LC_BUILD_VERSION)")


def version_key(text: str) -> tuple:
    return tuple(int(part) for part in text.split("."))


def check_floor(staged: Path, work: Path) -> None:
    """Hold the artifact to the oldest system it claims, and print what that is.

    A program is built with the packaged compiler, from a directory outside the
    checkout and without MACOSX_DEPLOYMENT_TARGET, the way a user builds one.

    - **macOS** fails unless the compiler states the LLVM floor setup_llvm.py
      recorded and the program states package.py's MACOS_FLOOR. Both used to be
      the build machine's macOS.
    - **Windows** fails when anything imports the Visual C++ runtime DLLs
      (VCRUNTIME*, MSVCP*): they are not on a fresh Windows, and the UCRT is.
    - **Linux** prints the newest glibc symbol version and the shared libraries
      needed, and fails on nothing yet: glibc binds each symbol to the build
      machine's version, so the floor is whichever distribution built the
      archive. Build it on the oldest one the release supports.
    """
    compiler = staged / "bin" / f"prismio{EXE}"
    source = work / "floor.psm"
    source.write_text("import std.io\n\nfn main() -> Int {\n    println(\"floor\")\n"
                      "    return 0\n}\n")
    program = work / f"floor{EXE}"
    env = os.environ.copy()
    env.pop("MACOSX_DEPLOYMENT_TARGET", None)
    built = subprocess.run([str(compiler), "build", str(source), "-o", str(program)],
                           capture_output=True, text=True, cwd=str(work), env=env)
    if built.returncode != 0:
        die("the packaged compiler could not build a program:\n" + built.stdout + built.stderr)
    if "different target triples" in built.stdout + built.stderr:
        die("the runtime bitcode and the program disagree on the target triple:\n"
            + built.stdout + built.stderr)
    ran = subprocess.run([str(program)], capture_output=True, text=True)
    if ran.returncode != 0 or ran.stdout.strip() != "floor":
        die(f"the program the packaged compiler built did not run ({ran.returncode})")

    if sys.platform == "darwin":
        sys.path.insert(0, str(REPO / "tools"))
        from package import MACOS_FLOOR
        info = json.loads((REPO / "third_party" / "llvm-paths.json").read_text())
        wanted = info.get("macos_min") or die(
            "third_party/llvm-paths.json records no macos_min",
            "re-run python3 tools/setup_llvm.py")
        for binary, floor in ((compiler, wanted), (program, MACOS_FLOOR)):
            stated = macos_minos(binary)
            if version_key(stated) > version_key(floor):
                die(f"{binary.name} needs macOS {stated}, but the release supports {floor}",
                    "was it built before setup_llvm.py recorded macos_min? "
                    "re-run setup_llvm.py, then `prismio build`")
        print(f"   ok -- the compiler runs on macOS {macos_minos(compiler)}+, "
              f"and builds programs for {macos_minos(program)}+")
    elif WINDOWS:
        needed = {}
        for binary in [compiler, program, *sorted((staged / "bin").glob("*.dll"))]:
            r = run([llvm_objdump(), "--private-headers", binary])
            names = re.findall(r"DLL Name: (\S+)", r.stdout)
            needed[binary.name] = names
            redist = [n for n in names if re.match(r"(?i)(vcruntime|msvcp)", n)]
            if redist:
                die(f"{binary.name} imports {', '.join(redist)}, the Visual C++ runtime, "
                    "which a fresh Windows does not have",
                    "link the static CRT (/MT), or ship those DLLs beside it")
        for name, names in needed.items():
            print(f"   {name}: {', '.join(names)}")
        print("   ok -- nothing needs the Visual C++ redistributable")
    else:
        for binary in (compiler, program):
            r = run([llvm_objdump(), "-T", "-p", binary])
            versions = set(re.findall(r"GLIBC_([0-9.]+)", r.stdout))
            libraries = re.findall(r"NEEDED\s+(\S+)", r.stdout)
            newest = max(versions, key=version_key) if versions else "?"
            print(f"   {binary.name}: glibc {newest}+; needs {', '.join(libraries)}")


def build_release_compiler(host: Path) -> Path:
    """`host build --release` in this checkout; the compiler it produced.

    The release profile, so the build writes `.prismio/build/release/` and never
    touches the debug-profile host that `prismio release` itself is running.
    """
    print(f"== building the compiler to ship (release profile, with {host.name})")
    built = subprocess.run([str(host), "build", "--release"], cwd=str(REPO))
    if built.returncode != 0:
        die("`build --release` failed",
            "if src/ uses something this host cannot compile, run `prismio build` first")
    compiler = REPO / ".prismio" / "build" / "release" / f"prismio{EXE}"
    if not compiler.is_file():
        die(f"`build --release` produced no {compiler.relative_to(REPO)}")
    return compiler


def bootstrap(compiler: Path, out: Path) -> subprocess.CompletedProcess:
    if WINDOWS:
        shell = shutil.which("pwsh") or shutil.which("powershell")
        return run([shell, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                    REPO / "tools" / "bootstrap.ps1", "-Compiler", compiler, "-Out", out])
    return run(["bash", REPO / "tools" / "bootstrap.sh",
                "--compiler", compiler, "--out", out])


def main() -> int:
    parser = argparse.ArgumentParser(description="Build release artifacts and checksums.")
    chosen = parser.add_mutually_exclusive_group(required=True)
    chosen.add_argument("--compiler", help="ship this compiler binary as it is")
    chosen.add_argument("--build-with", metavar="COMPILER",
                        help="build the compiler to ship from this checkout with COMPILER")
    parser.add_argument("--version")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    given = resolve_executable(args.build_with or args.compiler)
    if not given.is_file():
        die(f"no compiler at {given}")
    compiler = build_release_compiler(given) if args.build_with else given

    # Every compiler below is named `prismio` and runs inside this project, and
    # a `prismio` there forwards to build.ums's toolchain.host -- the fixpoint
    # check would test the debug host, not the compiler being shipped. Hosted
    # means "you are the compiler; do the work yourself", as package.py says too.
    os.environ["PRISMIO_INTERNAL_HOSTED"] = "1"

    version = reported_version(compiler)
    if args.version and args.version != version:
        die(f"--version {args.version} but the compiler reports {version}",
            "PRISMIO_VERSION in src/main.psm is the source of truth.")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    out = out.resolve()

    work = Path(tempfile.mkdtemp(prefix="prismio-release-"))
    try:
        print("== fixpoint check")
        if bootstrap(compiler, work / f"gen{EXE}").returncode != 0:
            die("could not build the next generation from this compiler")
        frozen, following = work / "frozen.ll", work / "next.ll"
        if run([compiler, "build", "src/main.psm", "-o", frozen]).returncode != 0:
            die("the frozen compiler could not build src/main.psm")
        if run([work / f"gen{EXE}", "build", "src/main.psm", "-o", following]).returncode != 0:
            die("the next generation could not build src/main.psm")
        if not filecmp.cmp(frozen, following, shallow=False):
            die(f"{compiler} is not a fixpoint -- it does not reproduce its own IR")
        print("   ok -- the frozen compiler reproduces its own IR")

        stem = f"prismio-{version}-{host_triple()}"
        print(f"== packaging {stem}")
        staged = work / stem
        if staged.exists():
            shutil.rmtree(staged)
        packaged = run([sys.executable, "tools/package.py",
                        "--compiler", compiler, "--out", staged])
        if packaged.returncode != 0:
            die("packaging failed:\n" + packaged.stdout + packaged.stderr)
        separated = run([sys.executable, "tools/verify_separation.py", "--dist", staged])
        if separated.returncode != 0:
            die("the packaged toolchain failed its separation checks")

        print("== the oldest system it runs on")
        check_floor(staged, work)
        for extra in ("LICENSE", "CHANGELOG.md"):
            if (REPO / extra).is_file():
                shutil.copyfile(REPO / extra, staged / extra)

        print("== archiving")
        archive_format = "zip" if WINDOWS else "gztar"
        suffix = ".zip" if WINDOWS else ".tar.gz"
        archive = Path(shutil.make_archive(str(out / stem), archive_format,
                                           root_dir=str(work), base_dir=stem))
        if archive.name != stem + suffix:
            archive = archive.rename(out / (stem + suffix))

        print("== checksums")
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        line = f"{digest}  {archive.name}\n"
        checksum = out / (archive.name + ".sha256")
        checksum.write_text(line, encoding="ascii")
        print(line, end="")

        print()
        print(f"artifact: {archive}")
        print(f"checksum: {checksum}")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
