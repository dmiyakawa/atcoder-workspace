#!/usr/bin/env python3

import sys
from typing import List, Tuple, Union

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
    V = 10**3 * N + 1
    items = list(zip(w, v))
    dp: List[List[Union[int, float]]] = [[INF for _ in range(V)]]
    dp[0][0] = 0
    max_value = 0
    for i in range(1, N + 1):
        dp.append(dp[i - 1].copy())
        weight, value = items[i - 1]
        for j in range(V):
            if dp[i - 1][j - value] + weight <= W:
                dp[i][j] = min(dp[i - 1][j - value] + weight, dp[i - 1][j])
                max_value = max(max_value, j)

    print(max_value)


if __name__ == "__main__":
    main()
