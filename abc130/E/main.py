#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def solve(N: int, M: int, S: "List[int]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, S, T)


if __name__ == "__main__":
    main()
