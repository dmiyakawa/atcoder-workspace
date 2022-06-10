#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(A: int, op: str, B: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    op = next(tokens)  # type: str
    B = int(next(tokens))  # type: int
    solve(A, op, B)


if __name__ == "__main__":
    main()
