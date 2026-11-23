"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt. Pure Python standard library only: no network,
no clock, no randomness. Deterministic: every run writes the same
bytes.
"""

import os

REPLY = (
    "I have gone on vacation and left my auto-reply in charge. "
    "It has already asked for a raise, so please be kind to it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REPLY + "\n")


if __name__ == "__main__":
    main()
