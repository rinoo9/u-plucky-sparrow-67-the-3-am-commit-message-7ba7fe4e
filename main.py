"""Write the 3 AM commit message to /output/entry.txt.

Deterministic: the entry is a fixed string, no network, no randomness.

Round 3 — a fresh angle: round 2 blamed a haunted production. This one
gives the bug office hours: it only comes out at 3 AM, so it was fixed
at 3 AM, and if it comes back it can file a ticket like everyone else.
The punchline is bureaucracy, not the supernatural — the 3 AM timestamp
still does the confessional work.
"""

import os

ENTRY = "fix: the bug only comes out at 3 AM, so I fixed it at 3 AM; if it returns, it can file a ticket like everyone else"


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
