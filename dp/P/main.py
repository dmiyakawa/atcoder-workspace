#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


MOD = 1000000007  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N - 1)  # type: "List[int]"
    y = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


def solve(N: int, x: "List[int]", y: "List[int]"):
    return


if __name__ == "__main__":
    main()
