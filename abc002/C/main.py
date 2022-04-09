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
    x_a = int(next(tokens))  # type: int
    y_a = int(next(tokens))  # type: int
    x_b = int(next(tokens))  # type: int
    y_b = int(next(tokens))  # type: int
    x_c = int(next(tokens))  # type: int
    y_c = int(next(tokens))  # type: int
    solve(x_a, y_a, x_b, y_b, x_c, y_c)


def solve(x_a: int, y_a: int, x_b: int, y_b: int, x_c: int, y_c: int):
    a = x_b - x_a
    b = y_b - y_a
    c = x_c - x_a
    d = y_c - y_a
    print(abs(a * d - c * b) / 2)


if __name__ == "__main__":
    main()
