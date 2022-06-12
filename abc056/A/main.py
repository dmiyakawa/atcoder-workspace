#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(a: str, b: str):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = next(tokens)  # type: str
    b = next(tokens)  # type: str
    solve(a, b)


if __name__ == "__main__":
    main()
