#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, x: "List[int]", y: "List[int]", v: "List[int]", M: int, t: "List[str]", a: "List[int]", b: "List[int]"):
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
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        v[i] = int(next(tokens))
    M = int(next(tokens))  # type: int
    t = [str()] * (M)  # type: "List[str]"
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        t[i] = next(tokens)
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, x, y, v, M, t, a, b)


if __name__ == "__main__":
    main()
