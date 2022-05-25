#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    h = int(next(tokens))  # type: int
    w = int(next(tokens))  # type: int
    solve(H, W, h, w)


def solve(H: int, W: int, h: int, w: int):
    return


if __name__ == "__main__":
    main()
