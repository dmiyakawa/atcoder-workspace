#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, T: "List[int]", M: int, P: "List[int]", X: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    X = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, T, M, P, X)


if __name__ == "__main__":
    main()
