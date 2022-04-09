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
    solve(N, M)


def solve(N: int, M: int):
    for b in range(N + 1):
        n = N - b
        m = M - 3 * b
        a = (4 * n - m) // 2
        c = (m - 2 * n) // 2
        if a < 0 or c < 0 or (4 * n - m) % 2 == 1 or (m - 2 * n) % 2 == 1:
            continue
        print(a, b, c)
        return
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
