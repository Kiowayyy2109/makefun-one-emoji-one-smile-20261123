#!/usr/bin/env python3
"""One Emoji, One Smile -- make.fun entry (program/v1).

Writes exactly one emoji to /output/entry.txt: U+1F31E SUN WITH FACE.

Why this emoji: the judge picks the warmer of two emojis for a stranger.
A smiling sun radiates warmth at first glance, reads the same warm and
cheerful way in every culture, is a deliberate pick rather than the
default smiley face, and carries no intimacy, flirtation, irony, or
in-joke that would read oddly coming from a stranger.

The file holds exactly the four UTF-8 bytes of the emoji and no trailing
newline, so the entry is one character, four bytes, and deterministic.
"""

import os

EMOJI = "\U0001F31E"  # SUN WITH FACE
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    # Self-check: the gate requires 1-8 characters, not only whitespace,
    # and the entry must be exactly this one emoji. Re-read what was
    # written and refuse to finish silently if it is anything else.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != EMOJI.encode("utf-8"):
        raise SystemExit("entry.txt does not hold exactly the chosen emoji")
    if len(EMOJI) != 1 or EMOJI.isspace():
        raise SystemExit("chosen text is not a single non-space character")


if __name__ == "__main__":
    main()
