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
    t = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, K, t, d)


def solve(N: int, K: int, t: "List[int]", d: "List[int]"):
    return


if __name__ == "__main__":
    main()
