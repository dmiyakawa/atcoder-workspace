#!/usr/bin/env python3
import math
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
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


def solve(A: int, B: int):
    l = math.sqrt(A**2 + B**2)
    print(A/l, B/l)


if __name__ == "__main__":
    main()
