#!/usr/bin/env python3
"""Say What Actually Broke - make.fun entry.

Writes one line of software error copy to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "The Save button saved nothing. Your file is exactly where you left it, "
    "unsaved, because the disk filled up at 11:47 p.m. "
    "Free some space, then save again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
