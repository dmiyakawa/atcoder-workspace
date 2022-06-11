#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, a: "List[int]", b: "List[int]", Q: int, u: "List[int]", v: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    u = [int()] * (Q)  # type: "List[int]"
    v = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, M, a, b, Q, u, v)


if __name__ == "__main__":
    main()
