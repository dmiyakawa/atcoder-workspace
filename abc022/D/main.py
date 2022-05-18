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
    Ax = [int()] * (N)  # type: "List[int]"
    Ay = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        Ax[i] = int(next(tokens))
        Ay[i] = int(next(tokens))
    Bx = [int()] * (N)  # type: "List[int]"
    By = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        Bx[i] = int(next(tokens))
        By[i] = int(next(tokens))
    solve(N, Ax, Ay, Bx, By)


def solve(N: int, Ax: "List[int]", Ay: "List[int]", Bx: "List[int]", By: "List[int]"):
    return


if __name__ == "__main__":
    main()
