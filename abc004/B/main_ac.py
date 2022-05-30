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
    c = [[next(tokens) for _ in range(3 + 1)] for _ in range(3 + 1)]  # type: "List[List[str]]"
    solve(c)


def solve(c: "List[List[str]]"):
    c.reverse()
    for lst in c:
        lst.reverse()
        print(*lst)


if __name__ == "__main__":
    main()
