#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, x: "List[int]", y: "List[int]", a: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N - 1)  # type: "List[int]"
    y = [int()] * (N - 1)  # type: "List[int]"
    a = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(N, x, y, a)


if __name__ == "__main__":
    main()
