#!/usr/bin/env python3

import sys

input = sys.stdin.readline
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
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(H, W, a, b)


def solve(H: int, W: int, a: int, b: int):
    return


if __name__ == "__main__":
    main()
