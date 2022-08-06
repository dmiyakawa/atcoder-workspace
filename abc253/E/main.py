#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, M: int, K: int):
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dpc = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(M):
        dp[0][i] = 1
        dpc[0][i] = i + 1

    for i in range(1, N):
        for j in range(M):
            c = 0
            if K == 0:
                c += dpc[i - 1][M - 1]
            else:
                if j >= K:
                    c += dpc[i - 1][j - K]
                if j + K < M:
                    c += dpc[i - 1][M - 1] - dpc[i - 1][j + K - 1]
            dp[i][j] = c % MOD
            dpc[i][j] = (c + (dpc[i][j - 1] if j > 0 else 0)) % MOD
    print(dpc[N - 1][M - 1])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, M, K)


if __name__ == "__main__":
    main()
