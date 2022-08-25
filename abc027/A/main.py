#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(l: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    l = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(l)


if __name__ == "__main__":
    main()
