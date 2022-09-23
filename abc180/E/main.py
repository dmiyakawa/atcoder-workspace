#!/usr/bin/env python3
from functools import lru_cache

Inf = INF = float("INF")


def solve(N: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):
    d = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            a, b, c = X[i], Y[i], Z[i]
            p, q, r = X[j], Y[j], Z[j]
            d[i][j] = abs(p - a) + abs(q - b) + max(0, r - c)
            d[j][i] = abs(p - a) + abs(q - b) + max(0, c - r)

    # @lru_cache(maxsize=10**9)
    # def rec(S, u):
    #     if S == (1 << N) - 1 and u == 0:
    #         return 0
    #     ret = Inf
    #     for v in range(N):
    #         if not (S >> u & 1):
    #             ret = min(ret, d[u][v] + rec(S | 1 << u, v))
    #     return ret
    # print(rec(0, 0))

    dp = [[Inf] * N for _ in range(1 << N)]
    dp[(1 << N) - 1][0] = 0

    for S in range((1 << N) - 2, -1, -1):
        for u in range(N):
            for v in range(N):
                if not (S >> v & 1):
                    dp[S][u] = min(dp[S][u], d[u][v] + dp[S | 1 << v][v])
    print(dp[0][0])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    Z = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, X, Y, Z)


if __name__ == "__main__":
    main()
