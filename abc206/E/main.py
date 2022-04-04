#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(L, R)


def solve(L: int, R: int):
    return


if __name__ == "__main__":
    main()
