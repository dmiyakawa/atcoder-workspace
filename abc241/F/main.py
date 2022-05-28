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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    s_x = int(next(tokens))  # type: int
    s_y = int(next(tokens))  # type: int
    g_x = int(next(tokens))  # type: int
    g_y = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(H, W, N, s_x, s_y, g_x, g_y, X, Y)


def solve(H: int, W: int, N: int, s_x: int, s_y: int, g_x: int, g_y: int, X: "List[int]", Y: "List[int]"):
    return


if __name__ == "__main__":
    main()
