#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — writes one excuse line.

The program takes no input and needs no network. It writes exactly one
sentence (at most 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "I outsourced it to a subagent, who outsourced it to another subagent, who is currently writing this excuse."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
