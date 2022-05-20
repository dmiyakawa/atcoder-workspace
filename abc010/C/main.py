#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "YES"  # type: str
NO = "NO"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    tx_a = int(next(tokens))  # type: int
    ty_a = int(next(tokens))  # type: int
    tx_b = int(next(tokens))  # type: int
    ty_b = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    n = int(next(tokens))  # type: int
    x = [int()] * (n)  # type: "List[int]"
    y = [int()] * (n)  # type: "List[int]"
    for i in range(n):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(tx_a, ty_a, tx_b, ty_b, T, V, n, x, y)


def solve(tx_a: int, ty_a: int, tx_b: int, ty_b: int, T: int, V: int, n: int, x: "List[int]", y: "List[int]"):
    return


if __name__ == "__main__":
    main()
