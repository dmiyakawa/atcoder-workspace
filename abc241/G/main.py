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
    M = int(next(tokens))  # type: int
    W = [int()] * (M)  # type: "List[int]"
    L = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        W[i] = int(next(tokens))
        L[i] = int(next(tokens))
    solve(N, M, W, L)


def solve(N: int, M: int, W: "List[int]", L: "List[int]"):
    return


if __name__ == "__main__":
    main()
