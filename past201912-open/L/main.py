#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        c[i] = int(next(tokens))
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, x, y, c, X, Y, C)


def solve(N: int, M: int, x: "List[int]", y: "List[int]", c: "List[int]", X: "List[int]", Y: "List[int]", C: "List[int]"):
    return


if __name__ == "__main__":
    main()
