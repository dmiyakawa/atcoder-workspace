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
    X = float(next(tokens))  # type: float
    Y = float(next(tokens))  # type: float
    R = float(next(tokens))  # type: float
    solve(X, Y, R)


def solve(X: float, Y: float, R: float):
    return


if __name__ == "__main__":
    main()
