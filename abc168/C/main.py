#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(A: int, B: int, H: int, M: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(A, B, H, M)


if __name__ == "__main__":
    main()
