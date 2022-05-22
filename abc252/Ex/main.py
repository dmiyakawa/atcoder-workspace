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
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = [int()] * (N)  # type: "List[int]"
    V = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        D[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, C, K, D, V)


def solve(N: int, C: int, K: int, D: "List[int]", V: "List[int]"):
    return


if __name__ == "__main__":
    main()
