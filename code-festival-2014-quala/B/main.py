#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(A: str, B: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = next(tokens)  # type: str
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == "__main__":
    main()
