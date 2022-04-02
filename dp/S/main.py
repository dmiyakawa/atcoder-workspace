#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


MOD = 1000000007  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = next(tokens)  # type: str
    D = int(next(tokens))  # type: int
    solve(K, D)


def solve(K: str, D: int):
    return


if __name__ == "__main__":
    main()
