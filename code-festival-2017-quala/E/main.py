#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, M: int, A: str, B: str, C: str, D: str):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = next(tokens)  # type: str
    B = next(tokens)  # type: str
    C = next(tokens)  # type: str
    D = next(tokens)  # type: str
    solve(N, M, A, B, C, D)


if __name__ == "__main__":
    main()
