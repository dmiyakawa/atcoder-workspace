#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int

def solve(N: int, A: "List[int]"):
    # dp[i][j] ... i番目までオリジナルのAの要素を消費した状態で先頭がjである個数
    dp = [[0 for _ in range(10)] for _ in range(N)]
    for j in range(10):
        dp[0][j] = (1 if A[0] == j else 0)

    for i in range(1, N):
        for j in range(10):
            dp[i][(j + A[i]) % 10] = (dp[i][(j + A[i]) % 10] + dp[i - 1][j]) % MOD
            dp[i][(j * A[i]) % 10] = (dp[i][(j * A[i]) % 10] + dp[i - 1][j]) % MOD
    for j in range(10):
        print(dp[N - 1][j])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)





if __name__ == "__main__":
    main()
