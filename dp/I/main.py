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
    p = [float(next(tokens)) for _ in range(N)]  # type: "List[float]"
    solve(N, p)


def solve(N: int, p: "List[float]"):
    return


if __name__ == "__main__":
    main()