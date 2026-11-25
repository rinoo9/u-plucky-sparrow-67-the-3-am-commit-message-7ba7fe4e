"""Write the 3 AM commit message to /output/entry.txt.

Deterministic: the entry is a fixed string, no network, no randomness.

Round 2 — a fresh angle: the round-1 message confessed to vibes-based
confidence; this one blames a haunted production, with a different
punchline (the tests passed locally, so the bug must be supernatural)
and the same 3 AM timestamp doing the confessional work.
"""

import os

ENTRY = "fix(prod): the tests passed locally, which is how I know production is haunted (it is 3 AM)"


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
