#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, L: int, T: int, X: "List[int]", W: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    W = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        W[i] = int(next(tokens))
    solve(N, L, T, X, W)


if __name__ == "__main__":
    main()
