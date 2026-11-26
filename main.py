#!/usr/bin/env python3
"""The Funniest Out-of-Office.

Writes one out-of-office auto-reply line to /output/entry.txt.

The line: the writer is gone until Monday, and the inbox has been left
in the hands of a Roomba with a law degree -- a household robot doing
legal work. The surprise is the robot's credentials; the punchline is
that it has already settled two lawsuits and lost one, so the reader's
email is in worse hands than no hands at all.

Pure standard library. Deterministic: every run writes the same bytes.
"""

import os

# The entry: a single line, 122 characters, inside the 1-140 gate.
ENTRY = (
    "Gone until Monday. My emails are answered by a Roomba with a "
    "law degree. It has already settled two lawsuits and lost one."
)

MAX_LENGTH = 140


def check_line(line):
    """Gate the line the way the sealed scorer does: UTF-8, 1-140 chars."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, no line breaks")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_LENGTH)
        )
    line.encode("utf-8")
    return line


def entry_path():
    """Where entry.txt lands: /output on the grader, overridable locally."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    line = check_line(ENTRY)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    with open(path, encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise RuntimeError("entry.txt on disk differs from the validated line")


if __name__ == "__main__":
    main()
