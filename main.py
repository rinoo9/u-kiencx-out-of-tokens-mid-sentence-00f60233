#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence - make.fun entry.

Writes a single funny one-line error message to /output/entry.txt.
The line is a fixed string: fully deterministic, no randomness, no
network, no clock. Run it twice and the bytes are identical.
"""

import os

# The entry: one line, 62 characters (limit 140). The joke is the turn
# at the end - the error message itself ate the agent's last token.
LINE = "Error: I had one token left. I spent it on this error message."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
