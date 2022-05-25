#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n + 1)]  # type: "List[int]"
    solve(n, a)


def solve(n: int, a: "List[int]"):
    return


if __name__ == "__main__":
    main()
