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
    C = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C, h)


def solve(N: int, C: int, h: "List[int]"):
    return


if __name__ == "__main__":
    main()
