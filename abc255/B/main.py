#!/usr/bin/env python3
import math
import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, A: "List[int]", X: "List[int]", Y: "List[int]"):
    rad = 0
    for x, y in zip(X, Y):
        min_rad = Inf
        for i in A:
            x0, y0 = X[i - 1], Y[i - 1]
            min_rad = min(min_rad, math.sqrt((x-x0)**2 + (y-y0)**2))
            if min_rad == 0:
                break
        rad = max(min_rad, rad)
    print(rad)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, K, A, X, Y)


if __name__ == "__main__":
    main()
