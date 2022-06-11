#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, xmin: "List[int]", ymin: "List[int]", D: "List[int]", C: "List[int]", A: "List[int]", B: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    xmin = [int()] * (N)  # type: "List[int]"
    ymin = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        xmin[i] = int(next(tokens))
        ymin[i] = int(next(tokens))
        D[i] = int(next(tokens))
        C[i] = int(next(tokens))
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, Q, xmin, ymin, D, C, A, B)


if __name__ == "__main__":
    main()
