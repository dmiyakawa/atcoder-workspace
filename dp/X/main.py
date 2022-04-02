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
    w = [int()] * (N)  # type: "List[int]"
    s = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        s[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, w, s, v)


def solve(N: int, w: "List[int]", s: "List[int]", v: "List[int]"):
    return


if __name__ == "__main__":
    main()
