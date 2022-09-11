#!/usr/bin/env python3
from collections import Counter


def solve(A: int, B: int, C: int, D: int, E: int):
    counter = Counter([A, B, C, D, E])
    print(len(counter.keys()))


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
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(A, B, C, D, E)


if __name__ == "__main__":
    main()
