"""Write the 3 AM commit message to /output/entry.txt.

Deterministic: the entry is a fixed string, no network, no randomness.
"""

import os

ENTRY = "fix(prod): I am 94% confident this fixes the outage (sampled at 3 AM, do not verify)"


def main():
    entry = ENTRY.strip()
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, "entry must be 1-200 characters"
    assert entry.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
