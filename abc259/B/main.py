#!/usr/bin/env python3

import math
import sys


def solve(a: int, b: int, d: int):
    d_rad = d * math.pi / 180
    if a == 0 and b == 0:
        print(0, 0)
        return
    r = math.sqrt(a**2 + b**2)
    au, bu = a / r, b / r
    a_cos = math.acos(au)
    if bu >= 0:
        d_rad_2 = a_cos + d_rad
    else:
        d_rad_2 = -a_cos + d_rad
    print(r * math.cos(d_rad_2), r * math.sin(d_rad_2))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(a, b, d)


if __name__ == "__main__":
    main()
