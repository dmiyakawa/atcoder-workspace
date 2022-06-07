#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(H: int, W: int, M: int, h: "List[int]", w: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    h = [int()] * (M)  # type: "List[int]"
    w = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        h[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(H, W, M, h, w)


if __name__ == "__main__":
    main()
