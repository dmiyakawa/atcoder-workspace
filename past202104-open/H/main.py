#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, K: int, Q: int, P: "List[int]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    P = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        P[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(N, M, K, Q, P, T)


if __name__ == "__main__":
    main()
