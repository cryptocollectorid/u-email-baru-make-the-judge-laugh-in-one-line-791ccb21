#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes a single funny line to /output/entry.txt.
"""

import os

LINE = "My robot vacuum joined a union. Now it only cleans the rooms it believes in — and it believes in none of them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
