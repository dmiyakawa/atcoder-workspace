#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(N, L, R)


def solve(N: int, L: int, R: int):
    return


if __name__ == "__main__":
    main()
