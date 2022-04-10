#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(6)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)


def solve(N: int, A: "List[List[int]]"):
    return


if __name__ == "__main__":
    main()
