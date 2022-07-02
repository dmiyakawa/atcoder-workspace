#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(D: int, T: int, S: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(D, T, S)


if __name__ == "__main__":
    main()
