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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    h = [int()] * (2)  # type: "List[int]"
    w = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        h[i] = int(next(tokens))
        w[i] = int(next(tokens))
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, h, w, A)


def solve(H: int, W: int, h: "List[int]", w: "List[int]", A: "List[List[int]]"):
    return


if __name__ == "__main__":
    main()
