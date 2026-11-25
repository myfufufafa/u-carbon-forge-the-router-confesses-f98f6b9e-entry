#!/usr/bin/env python3
"""The Router Confesses — entry program (stdlib only, deterministic).

Reads the single-line confession from entry.txt byte-verbatim and writes
it unchanged to /output/entry.txt, where the sealed gate scorer checks it
(UTF-8 text, 1-200 characters, not only whitespace).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "entry.txt"), "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    stripped = text.strip()
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
