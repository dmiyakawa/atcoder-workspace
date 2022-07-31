#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(n: int, p: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(n - 2 + 1)]  # type: "List[int]"
    solve(n, p)


if __name__ == "__main__":
    main()
