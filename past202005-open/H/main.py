#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, L: int, x: "List[int]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(N, L, x, T)


if __name__ == "__main__":
    main()
