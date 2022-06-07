#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def solve(r: "List[int]", c: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    r = [int()] * (2)  # type: "List[int]"
    c = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(r, c)


if __name__ == "__main__":
    main()
