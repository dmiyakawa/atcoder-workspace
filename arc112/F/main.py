#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1  # type: int


def solve(n: int, m: int, c: "List[int]", s: "List[List[int]]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    s = [[int(next(tokens)) for _ in range(n)] for _ in range(m)]  # type: "List[List[int]]"
    solve(n, m, c, s)


if __name__ == "__main__":
    main()
