#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, A: "List[int]", T: "List[int]", X: "List[int]", Y: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int()] * (Q)  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, Q, A, T, X, Y)


if __name__ == "__main__":
    main()
