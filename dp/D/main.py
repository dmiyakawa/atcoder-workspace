#!/usr/bin/env python3

import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    items = list(zip(w, v))
    dp: List[List[int]] = [[-1 for _ in range(W + 1)]]
    dp[0][0] = 0
    for i in range(1, N + 1):
        dp.append(dp[i - 1].copy())
        weight = items[i - 1][0]
        value = items[i - 1][1]
        for j in range(W + 1):
            if j + weight <= W:
                dp[i][j + weight] = max(dp[i - 1][j] + value, dp[i - 1][j + weight])
    print(max(dp[N]))


if __name__ == "__main__":
    main()
