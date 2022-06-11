#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, P: "List[int]", U: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int()] * (N)  # type: "List[int]"
    U = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        P[i] = int(next(tokens))
        U[i] = int(next(tokens))
    solve(N, P, U)


if __name__ == "__main__":
    main()
