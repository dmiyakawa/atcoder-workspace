#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, Q: int, K: int, a: "List[int]", u: "List[int]", v: "List[int]", s: "List[int]", t: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    s = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, M, Q, K, a, u, v, s, t)


if __name__ == "__main__":
    main()
