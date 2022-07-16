#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, U: "List[int]", V: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    U = [int()] * (N - 1)  # type: "List[int]"
    V = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, U, V)


if __name__ == "__main__":
    main()
