#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")

cache = {1: "1"}


def main():
    N = int(input())
    print(" ".join(solve(N)))


def solve(N: int):
    if N == 1:
        return ["1"]
    else:
        if N in cache:
            return cache[N]

        ans = solve(N - 1) + [str(N)] + solve(N - 1)
        cache[N] = ans
        return ans


if __name__ == "__main__":
    main()
