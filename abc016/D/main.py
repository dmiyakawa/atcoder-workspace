#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A_x = int(next(tokens))  # type: int
    A_y = int(next(tokens))  # type: int
    B_x = int(next(tokens))  # type: int
    B_y = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(A_x, A_y, B_x, B_y, N, X, Y)


def solve(A_x: int, A_y: int, B_x: int, B_y: int, N: int, X: "List[int]", Y: "List[int]"):
    return


if __name__ == "__main__":
    main()
