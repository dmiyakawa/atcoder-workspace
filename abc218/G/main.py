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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, A, u, v)


def solve(N: int, A: "List[int]", u: "List[int]", v: "List[int]"):
    return


if __name__ == "__main__":
    main()
