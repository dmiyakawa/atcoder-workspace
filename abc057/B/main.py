#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (M)  # type: "List[int]"
    d = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, M, a, b, c, d)


if __name__ == "__main__":
    main()
