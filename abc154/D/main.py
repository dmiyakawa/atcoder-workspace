#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, p: "List[int]"):
    e2 = 0
    for i in range(K):
        pi = p[i]
        e2 += pi + 1
    max_e2 = e2
    for i in range(N - K):
        e2 -= p[i] + 1
        e2 += p[i + K] + 1
        max_e2 = max(max_e2, e2)
    print(max_e2 / 2)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, p)


if __name__ == "__main__":
    main()
