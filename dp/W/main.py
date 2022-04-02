#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


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
    a = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(N, M, l, r, a)


def solve(N: int, M: int, l: "List[int]", r: "List[int]", a: "List[int]"):
    return


if __name__ == "__main__":
    main()
