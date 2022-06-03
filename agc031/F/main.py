#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 2019  # type: int
YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(N: int, M: int, Q: int, MOD: int, A: "List[int]", B: "List[int]", C: "List[int]", S: "List[int]", T: "List[int]", R: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    MOD = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    S = [int()] * (Q)  # type: "List[int]"
    T = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, Q, MOD, A, B, C, S, T, R)


if __name__ == "__main__":
    main()
