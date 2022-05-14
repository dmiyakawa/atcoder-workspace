#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = [int()] * (K)  # type: "List[int]"
    R = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, K, L, R)


def solve(N: int, K: int, L: "List[int]", R: "List[int]"):
    return


if __name__ == "__main__":
    main()
