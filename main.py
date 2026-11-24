#!/usr/bin/env python3
"""Fortune in a Pot: a kind, funny fortune for a houseplant.

Writes one line to /output/entry.txt: a fortune for the little pothos
on the windowsill. Stdlib only, no network, deterministic.
"""

import os

FORTUNE = "Thursday brings rain for your leaves, little pothos, and the cat has sworn, at last, never to taste you again."

OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
