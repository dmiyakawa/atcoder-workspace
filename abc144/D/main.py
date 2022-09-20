#!/usr/bin/env python3
import math


def solve(a: int, b: int, x: int):
    l = (a * a * b - x) * 2 / (a * a)
    if l > b:
        theta = math.atan2(2 * x / (a * b), b)
    else:
        theta = math.atan2(a, l)
    print(90 - theta * 180 / math.pi)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    solve(a, b, x)





if __name__ == "__main__":
    main()
