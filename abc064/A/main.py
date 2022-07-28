#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(r: int, g: int, b: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    r = int(next(tokens))  # type: int
    g = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(r, g, b)


if __name__ == "__main__":
    main()
