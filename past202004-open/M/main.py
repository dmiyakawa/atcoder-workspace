#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(D: int, L: int, N: int, C: "List[int]", K: "List[int]", F: "List[int]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(D)]  # type: "List[int]"
    K = [int()] * (N)  # type: "List[int]"
    F = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        K[i] = int(next(tokens))
        F[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(D, L, N, C, K, F, T)


if __name__ == "__main__":
    main()
