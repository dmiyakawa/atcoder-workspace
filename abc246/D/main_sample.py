#!/usr/bin/env python3
#
# 解説より
# https://atcoder.jp/contests/abc246/editorial/3701
#

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


def func(a, b):
    return a*a*a + a*a*b + a*b*b + b*b*b


def solve(N: int):
    min_n = INF
    b = 10**6
    for a in range(0, 10**6):
        while func(a, b) >= N and b >= 0:
            min_n = min(func(a, b), min_n)
            b -= 1
    print(min_n)


if __name__ == "__main__":
    main()
