#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, L: int, R: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(S, L, R)


if __name__ == "__main__":
    main()
