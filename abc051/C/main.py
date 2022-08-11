#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(sx: int, sy: int, tx: int, ty: int):
    x, y = tx - sx, ty - sy
    r1 = ("U" * y) + ("R" * x) + ("D" * y) + ("L" * x)
    r2 = "L" + ("U" * (y + 1)) + ("R" * (x + 1)) + "D"
    r3 = "R" + ("D" * (y + 1)) + ("L" * (x + 1)) + "U"
    print(r1 + r2 + r3)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    sx = int(next(tokens))  # type: int
    sy = int(next(tokens))  # type: int
    tx = int(next(tokens))  # type: int
    ty = int(next(tokens))  # type: int
    solve(sx, sy, tx, ty)


if __name__ == "__main__":
    main()
