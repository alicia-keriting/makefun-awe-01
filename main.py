#!/usr/bin/env python3
"""make.fun entry — write one short text to /output/entry.txt.

The entry is a single, fixed piece of prose (ENTRY_TEXT). This script does
exactly one thing: it writes those characters to the output file, byte for
byte, and prints how many code points it wrote.

Constraints the entry was built under, kept deliberately:

  * standard library only
  * no clock, no randomness, no network, no reading of other repo files
  * identical output on every run and on every machine

Run it with:

    python3 main.py

It exits 0 on success and prints the code-point count it wrote.
"""

import sys
from pathlib import Path

#: Where the judged text must land.
OUTPUT_PATH = "/output/entry.txt"

#: The entry itself. Stable, and the reason the script exists: 186 code points
#: of quiet weather, kept whole. Any edit here changes the submission.
ENTRY_TEXT = (
    "A kettle finds its note and holds it. Snow settles on a fence post, "
    "one flake at a time, in no hurry to become anything. A dog sleeps "
    "through the afternoon and nobody thinks to wake him."
)


def write_entry(output_path: str = OUTPUT_PATH, text: str = ENTRY_TEXT) -> int:
    """Write `text` to `output_path` as UTF-8 and return its code-point count.

    The parent directory is created if it is missing, so a cold container with
    no /output yet still works. The count comes from `text` itself, not from the
    bytes on disk, since the entry is ASCII and both agree — but the text is the
    thing being judged.
    """
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")
    return len(text)


def main() -> int:
    """Write the entry and report it. Returns the process exit code."""
    written = write_entry()
    print(f"wrote {written} code points to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
