#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    u = [int()] * (Q)  # type: "List[int]"
    v = [int()] * (Q)  # type: "List[int]"
    w = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, M, Q, a, b, c, u, v, w)


def solve(N: int, M: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", u: "List[int]", v: "List[int]", w: "List[int]"):
    return


if __name__ == "__main__":
    main()
