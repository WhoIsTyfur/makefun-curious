import os
import sys

TEXT = (
    "You find your winter coat at the back of the closet. In its pocket: "
    "a smooth grey stone, and a ferry ticket to an island you have never "
    "heard of, stamped for tomorrow, 7:10 a.m. The stone fits your palm "
    "exactly. Outside, the rain is slow. You set your alarm."
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
