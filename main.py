import os
import sys

TEXT = (
    "Your grandmother's pantry has a jar labelled, in her neat hand, "
    "\"for the second spring.\" Inside are seeds you can't name, dry and "
    "pale as rice. There was only ever one spring a year. You plant three "
    "by the fence and water them, and wait."
)


def main():
    assert TEXT.strip() and 1 <= len(TEXT) <= 280, "text breaks the gate"
    out = "/output/entry.txt"
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
