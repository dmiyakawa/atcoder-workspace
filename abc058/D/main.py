#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def solve(n: int, m: int, x: "List[int]", y: "List[int]"):

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    y = [int(next(tokens)) for _ in range(m)]  # type: "List[int]"
    solve(n, m, x, y)


if __name__ == "__main__":
    main()
