#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(X: int, Y: int, A: int, B: int):
    ans = 0
    while True:
        x1 = X * A
        x2 = X + B
        if x1 >= Y and x2 >= Y:
            break
        if x1 < x2:
            ans += 1
            X = x1
        else:
            ans += (Y - 1 - X) // B
            break

    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(X, Y, A, B)


if __name__ == "__main__":
    main()
