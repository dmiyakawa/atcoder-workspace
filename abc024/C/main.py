#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, D: int, K: int, L: "List[int]", R: "List[int]", S: "List[int]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = [int()] * (D)  # type: "List[int]"
    R = [int()] * (D)  # type: "List[int]"
    for i in range(D):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    S = [int()] * (K)  # type: "List[int]"
    T = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(N, D, K, L, R, S, T)


if __name__ == "__main__":
    main()
