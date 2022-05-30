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
    S = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(S, T, X)


def solve(S: int, T: int, X: int):
    return


if __name__ == "__main__":
    main()
