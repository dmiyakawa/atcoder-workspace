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
    X = next(tokens)  # type: str
    solve(X)


def solve(X: str):
    return


if __name__ == "__main__":
    main()
