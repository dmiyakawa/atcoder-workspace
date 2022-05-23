#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    p = [int()] * (K)  # type: "List[int]"
    q = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    r = [int()] * (L)  # type: "List[int]"
    s = [int()] * (L)  # type: "List[int]"
    for i in range(L):
        r[i] = int(next(tokens))
        s[i] = int(next(tokens))
    solve(N, K, L, p, q, r, s)


def solve(N: int, K: int, L: int, p: "List[int]", q: "List[int]", r: "List[int]", s: "List[int]"):
    return


if __name__ == "__main__":
    main()
