#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, X: int, P: "List[int]", C: "List[int]", L: "List[int]", R: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int()] * (Q)  # type: "List[int]"
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        C[i] = int(next(tokens))
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, Q, X, P, C, L, R)


if __name__ == "__main__":
    main()
