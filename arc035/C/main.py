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
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    X = [int()] * (K)  # type: "List[int]"
    Y = [int()] * (K)  # type: "List[int]"
    Z = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, M, A, B, C, K, X, Y, Z)


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]", K: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):
    return


if __name__ == "__main__":
    main()
