#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(A: "List[List[int]]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(9)] for _ in range(9)]  # type: "List[List[int]]"
    solve(A)


if __name__ == "__main__":
    main()
