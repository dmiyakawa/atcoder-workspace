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
    T = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    u = [int()] * (T)  # type: "List[int]"
    v = [int()] * (T)  # type: "List[int]"
    for i in range(T):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, T, L, u, v)


def solve(N: int, T: int, L: int, u: "List[int]", v: "List[int]"):
    return


if __name__ == "__main__":
    main()
