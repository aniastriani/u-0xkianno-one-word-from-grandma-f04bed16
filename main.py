"""One Word From Grandma.

Writes exactly one word to /output/entry.txt: the word a grandma
says when you walk through her door. Pure Python standard library.
"""

import os

WORD = "Sweetheart"
# One word, the way grandma says it: not a sentence, not a speech,
# just the name she has called you since you were small enough to
# sit on her lap. Warmth that fits in a single breath.


def main():
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
