#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(S: str, T: str, A: int, B: int, U: str):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    U = next(tokens)  # type: str
    solve(S, T, A, B, U)


if __name__ == "__main__":
    main()
