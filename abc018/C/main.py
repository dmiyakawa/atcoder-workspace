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
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(R)]  # type: "List[str]"
    solve(R, C, K, s)


def solve(R: int, C: int, K: int, s: "List[str]"):
    lst = [[1] * C for _ in range(R)]
    print(R, C, K)
    for r in range(K - 1):
        for c in range(K - 1, C - K + 1):
            for r2 in range(r, r + K):
            print(r, c)
    for r in range(K - 1, R - K + 1):
        for c in range(C):
            print(r, c)
    for r in range(R - K + 1, R):
        for c in range(K - 1, C - K + 1):
            print(r, c)


if __name__ == "__main__":
    main()
