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
    a = [int(next(tokens)) for _ in range(9 + 1)]  # type: "List[int]"
    solve(a)


def solve(a: "List[int]"):
    return


if __name__ == "__main__":
    main()
