#!/usr/bin/env python3

import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


MOD = 1000000007  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [[next(tokens) for _ in range(1)] for _ in range(H)]  # type: "List[List[str]]"
    solve(H, W, a)


def solve(H: int, W: int, a: "List[List[str]]"):
    dp: List[List[int]] = [[0] * W]
    for h in range(H):
        dp.append(dp[h - 1].copy())
        for w in range(W):
            if a[h][w] == "#":
                dp[h][w] = 0
            elif w == 0:
                if h > 0:
                    dp[w][h] = dp[w][h - 1]
            else:
                if h == 0:
                    dp[w][h] = dp[w - 1][h]
                else:
                    dp[w][h] = (dp[w - 1][h] + dp[w][h - 1]) % MOD
    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    main()
