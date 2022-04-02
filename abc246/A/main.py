#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    x = [int()] * (3)  # type: "List[int]"
    y = [int()] * (3)  # type: "List[int]"
    for i in range(3):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(x, y)


def solve(X: "List[int]", Y: "List[int]"):
    x_set = set()
    y_set = set()
    for x in X:
        if x in x_set:
            x_set.discard(x)
        else:
            x_set.add(x)
    for y in Y:
        if y in y_set:
            y_set.discard(y)
        else:
            y_set.add(y)
    print(x_set.pop(), y_set.pop())


if __name__ == "__main__":
    main()
