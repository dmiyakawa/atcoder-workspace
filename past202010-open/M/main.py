#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, a: "List[int]", b: "List[int]", u: "List[int]", v: "List[int]", c: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    u = [int()] * (Q)  # type: "List[int]"
    v = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, Q, a, b, u, v, c)


if __name__ == "__main__":
    main()
