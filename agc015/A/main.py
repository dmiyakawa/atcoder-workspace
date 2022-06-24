#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: int, B: int):
    if A > B:
        print(0)
        return
    min_val = (N - 1) * A + B
    max_val = (N - 1) * B + A
    print(max(max_val - min_val + 1, 0))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)


if __name__ == "__main__":
    main()
