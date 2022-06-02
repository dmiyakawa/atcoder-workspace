#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, M: int, K: int):
    dp = [[1] * M]
    dpc = [i for i in range(1, M + 1)]
    for i in range(1, N):
        for j in range(M):
            dp[i][]




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
