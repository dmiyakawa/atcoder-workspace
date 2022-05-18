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
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    T = [int()] * (M)  # type: "List[int]"
    K = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        T[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, M, X, Y, A, B, T, K)


def solve(N: int, M: int, X: int, Y: int, A: "List[int]", B: "List[int]", T: "List[int]", K: "List[int]"):
    return


if __name__ == "__main__":
    main()
