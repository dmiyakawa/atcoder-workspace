#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, W: int, v: "List[int]", w: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    v = [int()] * (N)  # type: "List[int]"
    w = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, W, v, w)


if __name__ == "__main__":
    main()
