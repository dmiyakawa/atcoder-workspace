#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, M: int, A: "List[int]", B: "List[int]", c: "List[List[int]]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    c = [[int(next(tokens)) for _ in range(M)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, M, A, B, c)


if __name__ == "__main__":
    main()