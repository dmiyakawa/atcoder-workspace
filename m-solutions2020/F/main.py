#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, X: "List[int]", Y: "List[int]", U: "List[str]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    U = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        U[i] = next(tokens)
    solve(N, X, Y, U)


if __name__ == "__main__":
    main()
