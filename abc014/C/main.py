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
    n = int(next(tokens))  # type: int
    a = [int()] * (n)  # type: "List[int]"
    b = [int()] * (n)  # type: "List[int]"
    for i in range(n):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(n, a, b)


def solve(n: int, a: "List[int]", b: "List[int]"):
    return


if __name__ == "__main__":
    main()
