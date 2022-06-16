#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, Q: int, D: "List[int]", L: "List[int]", R: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    D = [int()] * (Q)  # type: "List[int]"
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        D[i] = int(next(tokens))
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, Q, D, L, R)


if __name__ == "__main__":
    main()
