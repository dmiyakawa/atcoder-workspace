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
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, a, b, c)


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    dp = {0: {"a": a[0], "b": b[0], "c": c[0]}}
    for i in range(1, N):
        dp[i] = {"a": max(dp[i - 1]["b"], dp[i - 1]["c"]) + a[i],
                 "b": max(dp[i - 1]["a"], dp[i - 1]["c"]) + b[i],
                 "c": max(dp[i - 1]["a"], dp[i - 1]["b"]) + c[i]}
    print(max(dp[N - 1].values()))


if __name__ == "__main__":
    main()
