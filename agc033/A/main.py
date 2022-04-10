#!/usr/bin/env python3

import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    H, W = [int(e) for e in input().split()]
    A: List[str] = []
    for i in range(H):
        A.append(input().rstrip())
    pos = set()
    rows: List[List[float]] = [[0] * (W + 2)]
    for h, line in enumerate(A, start=1):
        row: List[float] = [0] * (W + 2)
        rows.append(row)
        for w, cell in enumerate(line, start=1):
            if cell == "#":
                pos.add((h, w))
                row[w] = 0
            else:
                row[w] = Inf
    rows.append([0] * (W + 2))
    num_steps = 0
    while pos:
        num_steps += 1
        next_pos = set()
        for h, w in pos:
            for nh, nw in [(h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)]:
                if rows[nh][nw] > num_steps:
                    rows[nh][nw] = num_steps
                    next_pos.add((nh, nw))
        pos = next_pos
    print(num_steps - 1)


if __name__ == "__main__":
    main()
