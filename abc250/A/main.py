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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(H, W, R, C)


def solve(H: int, W: int, R: int, C: int):
    return


if __name__ == "__main__":
    main()
