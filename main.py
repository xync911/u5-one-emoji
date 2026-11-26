"""Copy entry.txt to the output directory for the make.fun entry.

The entry is exactly one emoji and nothing else, at most 8
characters.
A smiling face with hearts: the warmest single character a
keyboard can send. No words, no caption, no explanation — the
warmth is the whole entry, and it needs nothing else.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
