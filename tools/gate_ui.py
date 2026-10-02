"""Terminal presentation shared by tools/gate.py and tools/release_gate.py.

One place decides colour, glyphs, column widths and durations, so the two scripts
print the same rows whether they run together under `prismio gate` or alone.

Colour follows the repository's other tools (off on Windows) plus the usual
conventions: `NO_COLOR` turns it off and `FORCE_COLOR` turns it on for a pipe.
The glyphs fall back to ASCII when the stream's encoding cannot print them, so a
legacy console or a log file never raises on the first check mark.
"""
import os
import re
import shutil
import sys
import threading
import time

WINDOWS = os.name == "nt"


def color_enabled() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    return sys.stdout.isatty() and not WINDOWS


def _unicode_ok() -> bool:
    try:
        "✓✗─·".encode(sys.stdout.encoding or "ascii")
        return True
    except (UnicodeEncodeError, LookupError):
        return False


COLOR = color_enabled()
FANCY = _unicode_ok()

CODES = {"bold": "1", "dim": "2", "red": "31", "green": "32", "yellow": "33", "cyan": "36"}

GLYPHS = {
    "ok": ("✓", "+"), "fail": ("✗", "x"), "warn": ("!", "!"),
    "skip": ("–", "-"), "run": ("·", "."),
}
KIND_COLOR = {"ok": "green", "fail": "red", "warn": "yellow", "skip": "dim", "run": "dim"}

TIME_WIDTH = 7


def style(text: str, *names: str) -> str:
    if not COLOR or not names:
        return text
    return "\033[" + ";".join(CODES[n] for n in names) + "m" + text + "\033[0m"


def glyph(kind: str) -> str:
    return style(GLYPHS[kind][0 if FANCY else 1], KIND_COLOR[kind])


def width() -> int:
    return max(64, min(shutil.get_terminal_size((100, 24)).columns, 110))


def rule(indent: int = 2) -> str:
    return " " * indent + style(("─" if FANCY else "-") * (width() - indent), "dim")


def duration(seconds: float) -> str:
    if seconds < 10:
        return f"{seconds:.1f}s"
    if seconds < 60:
        return f"{seconds:.0f}s"
    minutes, rest = divmod(round(seconds), 60)
    return f"{minutes}m {rest:02d}s"


def truncate(text: str, room: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if room <= 1:
        return ""
    if len(text) <= room:
        return text
    return text[:room - 1] + ("…" if FANCY else "~")


def row(kind: str, label: str, detail: str = "", seconds=None,
        label_width: int = 26, indent: int = 2, mark: str = "") -> str:
    """`  ✓ label                 detail                         1.2s`, fitted to the terminal."""
    lead = indent + 2 + label_width + 1  # indent, glyph, space, label, space
    room = width() - lead - TIME_WIDTH - 1
    shown = truncate(detail, room)
    elapsed = duration(seconds) if seconds is not None else ""
    label_text = style(label.ljust(label_width), "bold") if kind == "fail" else label.ljust(label_width)
    detail_text = style(shown, "red" if kind == "fail" else "dim")
    return (" " * indent + (mark or glyph(kind)) + " " + label_text + " " + detail_text
            + " " * (room - len(shown)) + " " + style(elapsed.rjust(TIME_WIDTH), "dim"))


SPINNER = ("\u280b\u2819\u2839\u2838\u283c\u2834\u2826\u2827\u2807\u280f", "|/-\\")


def live() -> bool:
    """Whether a status row can be redrawn in place (a terminal that takes ANSI)."""
    return COLOR and sys.stdout.isatty()


def clear_line() -> str:
    return "\r\033[K"


class Ticker:
    """One status row, redrawn in place while a check runs: a spinner, the label, where
    the check has got to, and the elapsed time. `end()` clears it for the finished row.

    On a pipe or a log file it does nothing: a redrawn line is noise there, and the
    finished rows already carry the result.
    """

    def __init__(self, label_width: int = 26, indent: int = 2):
        self.label_width, self.indent = label_width, indent
        self.lock = threading.Lock()
        self.thread = None
        self.stop = threading.Event()
        self.label = self.prefix = self.note_text = ""
        self.started = 0.0

    def begin(self, label: str, prefix: str = "") -> None:
        self.label, self.prefix, self.note_text = label, prefix, ""
        self.started = time.monotonic()
        if not live():
            return
        self.stop.clear()
        self._draw(0)
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def note(self, text: str) -> None:
        with self.lock:
            self.note_text = text

    def end(self) -> None:
        if self.thread is None:
            return
        self.stop.set()
        self.thread.join()
        self.thread = None
        with self.lock:
            sys.stdout.write(clear_line())
            sys.stdout.flush()

    def _loop(self) -> None:
        frame = 1
        while not self.stop.wait(0.12):
            self._draw(frame)
            frame += 1

    def _draw(self, frame: int) -> None:
        chars = SPINNER[0 if FANCY else 1]
        with self.lock:
            detail = f"{self.prefix} {self.note_text}".strip()
            line = row("run", self.label, detail, time.monotonic() - self.started,
                       self.label_width, self.indent, mark=style(chars[frame % len(chars)], "cyan"))
            sys.stdout.write(clear_line() + line)
            sys.stdout.flush()


def heading(text: str) -> str:
    return style(text, "bold")


def banner(index: int, total: int, title: str) -> str:
    return style(f"[{index}/{total}]", "dim") + " " + style(title, "bold", "cyan")


def verdict(passed: bool, text: str) -> str:
    return (style(" PASSED " if passed else " FAILED ", "bold", "green" if passed else "red")
            + " " + text)
