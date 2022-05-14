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
    N = int(next(tokens))  # type: int
    solve(N)


def solve(N: int):
    d = {}
    for a in range(1, 10):
        for b in range(1, 10):
            d.setdefault(2025 - a * b, []).append((a, b))
    for a, b in sorted(d[N]):
        print(f"{a} x {b}")


if __name__ == "__main__":
    main()
