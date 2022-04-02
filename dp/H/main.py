#!/usr/bin/env python3

import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 1000000007  # type: int


def main():
    H, W = [int(e) for e in input().split()]
    a = [input().rstrip() for _ in range(H)]
    dp: List[List[int]] = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if a[h][w] == "#":
                dp[h][w] = 0
            elif w == 0:
                if h > 0:
                    dp[h][w] = dp[h - 1][w]
            else:
                if h == 0:
                    dp[h][w] = dp[h][w - 1]
                else:
                    dp[h][w] = (dp[h][w - 1] + dp[h - 1][w]) % MOD
    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    main()
