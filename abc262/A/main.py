#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(Y: int):
    while True:
        if Y % 4 == 2:
            print(Y)
            return
        Y += 1


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    Y = int(next(tokens))  # type: int
    solve(Y)


if __name__ == "__main__":
    main()
