#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(X: int, Y: int):
    count_x = 0
    for x in range(1, X+1):
        if X % x == 0:
            count_x += 1
    count_y = 0
    for y in range(1, Y+1):
        if Y % y == 0:
            count_y += 1
    if count_x > count_y:
        print("X")
    elif count_x < count_y:
        print("Y")
    else:
        print("Z")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(X, Y)


if __name__ == "__main__":
    main()
