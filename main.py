#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Coffee is the vivid, punchy choice: an agent runs on caffeine, so A
lands as the fuller, more alive and funnier answer in this duel.
Deterministic: the same single byte on every run. No network,
no environment secrets, no input read at all.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Create the output directory if the sandbox has not made it yet,
    # then write the single byte atomically enough for a 1-byte file:
    # plain binary write, no newline, no encoding surprises.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(b"A")


if __name__ == "__main__":
    main()
