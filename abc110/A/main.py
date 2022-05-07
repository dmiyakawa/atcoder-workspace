#!/usr/bin/env python3
import itertools
import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


def solve(A: int, B: int, C: int):
    max_value = 0
    for a, b, c in itertools.permutations([A, B, C]):
        max_value = max(max_value, a * 10 + b + c)
    print(max_value)


if __name__ == "__main__":
    main()
