#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, f: "List[int]", t: "List[int]", x: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    f = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        f[i] = int(next(tokens))
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, Q, f, t, x)


if __name__ == "__main__":
    main()
