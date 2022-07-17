#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, X: int, Y: int):
    d = (1, 0)
    for i in range(N - 1):
        next_d = (d[0] + d[0] * X + d[1], (d[0] * X + d[1]) * Y)
        d = next_d
    print(d[1])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, X, Y)


if __name__ == "__main__":
    main()
