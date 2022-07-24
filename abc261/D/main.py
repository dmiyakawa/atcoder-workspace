#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, X: "List[int]", C: "List[int]", Y: "List[int]"):
    # i回目の試行時にカウンターがjになった際の最大値
    dp = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
    bonus_d = {c: y for c, y in zip(C, Y)}
    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1])
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1] + bonus_d.get(j, 0)

    print(max(dp[N]))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, X, C, Y)


if __name__ == "__main__":
    main()
