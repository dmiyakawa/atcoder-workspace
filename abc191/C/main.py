#!/usr/bin/env python3

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    H, W = map(int, input().split())
    S = [input().rstrip() for _ in range(H)]
    d = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                d[i][j] += 1
                d[i + 1][j] += 1
                d[i][j + 1] += 1
                d[i + 1][j + 1] += 1
    count = 0
    for i in range(H):
        for j in range(W):
            if d[i][j] == 1 or d[i][j] == 3:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
