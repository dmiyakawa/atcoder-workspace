#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(H: int, W: int, N: int, r: "List[int]", c: "List[int]", a: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    r = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    a = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(H, W, N, r, c, a)


if __name__ == "__main__":
    main()
