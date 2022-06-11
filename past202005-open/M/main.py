#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, u: "List[int]", v: "List[int]", s: int, K: int, t: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    s = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, M, u, v, s, K, t)


if __name__ == "__main__":
    main()
