#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(T: int, N: "List[int]", M: "List[int]", A: "List[int]", B: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    N = [int()] * (T)  # type: "List[int]"
    M = [int()] * (T)  # type: "List[int]"
    A = [int()] * (T)  # type: "List[int]"
    B = [int()] * (T)  # type: "List[int]"
    for i in range(T):
        N[i] = int(next(tokens))
        M[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(T, N, M, A, B)


if __name__ == "__main__":
    main()
