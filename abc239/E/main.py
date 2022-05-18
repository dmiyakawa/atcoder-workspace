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
    Q = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    V = [int()] * (Q)  # type: "List[int]"
    K = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        V[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, Q, X, A, B, V, K)


def solve(N: int, Q: int, X: "List[int]", A: "List[int]", B: "List[int]", V: "List[int]", K: "List[int]"):
    return


if __name__ == "__main__":
    main()
