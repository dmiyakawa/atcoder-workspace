#!/usr/bin/env python3
import math


def solve(A: int, B: int, N: int):
    x = min(B - 1, N)
    print(math.floor(A * x / B) - A * math.floor(x / B))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(A, B, N)


if __name__ == "__main__":
    main()
