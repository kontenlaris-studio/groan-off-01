#!/usr/bin/env python3
"""The One-Liner Groan-Off — make.fun entry.

One original dad joke, one line, at most 140 characters.
The alarm clock retires: six years of 5am starts, and the punch
lands on the word the whole joke was built for — "snoozed on",
the snooze button pressed a thousand mornings and being ignored,
in the same breath. The groan is the point.
"""

import os

ENTRY = "The alarm clock retired after 6 years — it said it was tired of being snoozed on."

assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, cap is 140"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
