#!/usr/bin/env python3
import math


def solve(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int):
    ba_x, ba_y = a_x - b_x, a_y - b_y
    bc_x, bc_y = c_x - b_x, c_y - b_y
    cb_x, cb_y = -bc_x, -bc_y
    ca_x, ca_y = a_x - c_x, a_y - c_y
    if ba_x * bc_x + ba_y * bc_y == 0:

        ...
    if ba_x * bc_x + ba_y * bc_y < 0:
        return math.sqrt(ba_x**2 + ba_y**2)
    if ca_x * cb_x + ca_y * cb_y < 0:
        return math.sqrt(ca_x**2 + ca_y**2)
    # あれ、一直線上にあるケースがなくない？？
    return abs(bc_x * ba_y - bc_y * ba_x) / math.sqrt(bc_x**2 + bc_y**2)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a_x = int(next(tokens))  # type: int
    a_y = int(next(tokens))  # type: int
    b_x = int(next(tokens))  # type: int
    b_y = int(next(tokens))  # type: int
    c_x = int(next(tokens))  # type: int
    c_y = int(next(tokens))  # type: int
    print(solve(a_x, a_y, b_x, b_y, c_x, c_y))


if __name__ == "__main__":
    main()
