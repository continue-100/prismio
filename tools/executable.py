"""An executable named the way build.ums names one: without `.exe`.

A manifest spells `.prismio/build/debug/prismio` once for every platform, and
the compiler itself appends `.exe` on Windows when it builds or starts a target
(umsExecutablePath). The tools a manifest command runs receive that spelling,
checked it with `is_file()`, and stopped with "no compiler at" on Windows --
`prismio dist`, `ship` and `verify` all did, and nothing noticed because CI
called the tools directly with `$EXT` appended.
"""
import os
from pathlib import Path


def resolve_executable(path) -> Path:
    """`path` as given if it exists, else with `.exe` on Windows, resolved."""
    candidate = Path(path)
    if not candidate.is_file() and os.name == "nt" and candidate.suffix.lower() != ".exe":
        with_suffix = candidate.with_name(candidate.name + ".exe")
        if with_suffix.is_file():
            candidate = with_suffix
    return candidate.resolve()
