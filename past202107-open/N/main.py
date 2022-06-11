#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(Q: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    C = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(Q, A, B, C, D)


if __name__ == "__main__":
    main()
