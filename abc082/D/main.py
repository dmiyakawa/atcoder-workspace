#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(s: str, x: int, y: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(s, x, y)


if __name__ == "__main__":
    main()
