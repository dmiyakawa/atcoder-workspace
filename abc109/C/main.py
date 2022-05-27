#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, x)


def solve(N: int, X: int, x: "List[int]"):
    return


if __name__ == "__main__":
    main()
