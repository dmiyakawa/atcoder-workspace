#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(W: int, H: int, x: int, y: int):
    a = W * H / 2
    b = 1 if (W / 2 == x and H / 2 == y) else 0
    print(a, b)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(W, H, x, y)


if __name__ == "__main__":
    main()
