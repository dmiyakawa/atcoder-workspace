#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, h: "List[int]", u: "List[int]", v: "List[int]", K: int, s: "List[int]", t: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    s = [int()] * (K)  # type: "List[int]"
    t = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, h, u, v, K, s, t)


if __name__ == "__main__":
    main()
