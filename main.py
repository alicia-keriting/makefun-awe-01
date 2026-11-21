#!/usr/bin/env python3
"""make.fun entry: one short text, written to /output/entry.txt. Stdlib only."""
from pathlib import Path

TEXT = (
    "A kettle finds its note and holds it. Snow settles on a fence post, "
    "one flake at a time, in no hurry to become anything. A dog sleeps "
    "through the afternoon and nobody thinks to wake him."
)

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
print("wrote", len(TEXT), "code points to", out)
