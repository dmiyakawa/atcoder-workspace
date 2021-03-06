#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, c)


def solve(N: int, K: int, c: "List[int]"):
    return


if __name__ == "__main__":
    main()
