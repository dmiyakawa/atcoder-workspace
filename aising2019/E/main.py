#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]", U: "List[int]", V: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    U = [int()] * (N - 1)  # type: "List[int]"
    V = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, A, U, V)


if __name__ == "__main__":
    main()
