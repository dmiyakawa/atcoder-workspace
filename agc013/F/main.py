#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]", Q: int, D: "List[int]", E: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    D = [int()] * (Q)  # type: "List[int]"
    E = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        D[i] = int(next(tokens))
        E[i] = int(next(tokens))
    solve(N, A, B, C, Q, D, E)


if __name__ == "__main__":
    main()
