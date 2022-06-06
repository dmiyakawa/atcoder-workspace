#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def solve(N: int, M: int, l: "List[int]", r: "List[int]", x: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    l = [int()] * (M)  # type: "List[int]"
    r = [int()] * (M)  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, M, l, r, x)


if __name__ == "__main__":
    main()
