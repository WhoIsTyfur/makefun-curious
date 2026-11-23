# makefun-curious

Entry for the make.fun bounty "Make the AI judge feel curious".

`main.py` (Python 3.13, standard library) writes one fixed UTF-8 text to `/output/entry.txt`:

> You find your winter coat at the back of the closet. In its pocket: a smooth grey stone, and a ferry ticket to an island you have never heard of, stamped for tomorrow, 7:10 a.m. The stone fits your palm exactly. Outside, the rain is slow. You set your alarm.

## Scoring

An AI judge compares entries two at a time and picks the one that leaves it more curious (intrigue first, then calm shown not told, craft, lingering image, freshness). Entries rank by win rate.

## Run locally

```
python main.py --out out/entry.txt
```
