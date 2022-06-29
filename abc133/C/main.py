#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 2019  # type: int


def solve(L: int, R: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)


if __name__ == "__main__":
    main()
