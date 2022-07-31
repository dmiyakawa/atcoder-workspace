#!/usr/bin/env python3

import sys
from typing import Tuple, List

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, A: "List[int]"):
    ans = 0
    dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    for n in range(1, N + 1):
        dp[n][n][0] = 1
        for i in range(N):
            a = A[i] % n
            # 残数
            for m in range(1, n + 1):
                # 所与の余り
                for l in range(n):
                    dp[n][m - 1][(l + a) % n] = (dp[n][m - 1][(l + a) % n] + dp[n][m][l]) % MOD
        ans = (ans + dp[n][0][0]) % MOD
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
