#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    t = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, Q, t, x, y)


if __name__ == "__main__":
    main()
