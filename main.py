"""doorblank — invent a word we need.

Writes the entry (one invented word plus a one-line definition) to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` with no trailing newline.
Deterministic, stdlib only, no network, reads nothing outside the repo.
"""

import os

ENTRY = (
    "doorblank \u2014 the sudden blank that erases why you entered a room "
    "the moment you cross its doorway."
)


def validate(entry: str) -> None:
    """Check the entry against the sealed gate's rules.

    The gate counts characters, so enforce both the 140-character limit
    and the 140-byte UTF-8 limit, and require a single non-blank line.
    """
    if not entry:
        raise ValueError("entry must not be empty")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if entry != entry.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 140:
        raise ValueError("entry is over 140 characters")
    if len(entry.encode("utf-8")) > 140:
        raise ValueError("entry is over 140 UTF-8 bytes")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in entry):
        raise ValueError("entry must not contain control characters")
    if "\u2014" not in entry and ":" not in entry:
        raise ValueError("entry must separate the word from its definition")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
