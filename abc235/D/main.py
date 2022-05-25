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
    a = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(a, N)


def solve(a: int, N: int):
    return


if __name__ == "__main__":
    main()
