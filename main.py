#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
/output/entry.txt. The label must be UTF-8 text of 1 to 160 characters,
not only whitespace. The program is deterministic: every run writes
the same line.
"""

import os

LABEL = (
    "WARNING: This human will nod as if it understood every word, "
    "then Google all of it the second you leave the room."
)


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 160, f"label is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "label must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
