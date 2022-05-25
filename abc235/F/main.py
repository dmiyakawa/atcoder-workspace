#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = next(tokens)  # type: str
    M = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, C)


def solve(N: str, M: int, C: "List[int]"):
    return


if __name__ == "__main__":
    main()
