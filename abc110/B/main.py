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
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    y = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X, Y, x, y)


def solve(N: int, M: int, X: int, Y: int, x: "List[int]", y: "List[int]"):
    print("No War" if X <= max(x) < min(y) <= Y else "War")


if __name__ == "__main__":
    main()
