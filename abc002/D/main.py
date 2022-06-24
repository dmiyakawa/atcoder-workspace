#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)


def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    d = {n: set() for n in range(1, N + 1)}
    for x_, y_ in zip(x, y):
        d[x_].add(y_)
        d[y_].add(x_)
    max_count = 1
    for n in range(1, N + 1):
        friends = d[n]
        new_friends = set()


if __name__ == "__main__":
    main()
