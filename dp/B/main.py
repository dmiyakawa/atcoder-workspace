#!/usr/bin/env python3

import sys

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
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)


def solve(N: int, K: int, h: "List[int]"):
    dp = {0: 0}
    for i in range(1, N):
        min_score = INF
        for j in range(1, K + 1):
            if i - j < 0:
                break
            min_score = min(dp[i - j] + abs(h[i - j] - h[i]), min_score)
        dp[i] = min_score
    print(dp[N - 1])


if __name__ == "__main__":
    main()
