#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, x: "List[int]", y: "List[int]", d: "List[str]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    d = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        d[i] = next(tokens)
    solve(N, x, y, d)


if __name__ == "__main__":
    main()
