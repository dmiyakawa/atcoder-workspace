#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, P: "List[int]", Q: int, U: "List[int]", D: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N - 2 + 1)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    U = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        U[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, P, Q, U, D)


if __name__ == "__main__":
    main()
