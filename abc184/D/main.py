#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(A: int, B: int, C: int):
    dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    for a in range(99, -1, -1):
        for b in range(99, -1, -1):
            for c in range(99, -1, -1):
                total = a + b + c
                ae = dp[a + 1][b][c] * a / total
                be = dp[a][b + 1][c] * b / total
                ce = dp[a][b][c + 1] * c / total
                dp[a][b][c] = 1 + ae + be + ce
                if (a, b, c) == (A, B, C):
                    return dp[a][b][c]


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    print(solve(A, B, C))


if __name__ == "__main__":
    main()
