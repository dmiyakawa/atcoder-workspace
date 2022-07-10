#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, X: int, T: int, D: int):
    if M >= X:
        return T
    return T - (X - M) * D


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    print(solve(N, M, X, T, D))


if __name__ == "__main__":
    main()
