#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, C: "List[int]", S: "List[int]", F: "List[int]"):
    dp = [[Inf for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
        for j in range(i + 1, N):
            s = max(dp[i][j - 1], S[j - 1])
            s = (s - s % F[j - 1] + F[j - 1]) if s % F[j - 1] > 0 else s
            dp[i][j] = s + C[j - 1]
    for i in range(N):
        print(dp[i][N - 1])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N - 1)  # type: "List[int]"
    S = [int()] * (N - 1)  # type: "List[int]"
    F = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        C[i] = int(next(tokens))
        S[i] = int(next(tokens))
        F[i] = int(next(tokens))
    solve(N, C, S, F)


if __name__ == "__main__":
    main()
