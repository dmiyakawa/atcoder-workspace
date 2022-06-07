#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, a: "List[int]", b: "List[int]", Q: int, t: "List[int]", e: "List[int]", x: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    t = [int()] * (Q)  # type: "List[int]"
    e = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        t[i] = int(next(tokens))
        e[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, a, b, Q, t, e, x)


if __name__ == "__main__":
    main()
