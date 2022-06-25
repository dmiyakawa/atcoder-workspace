#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(M: int, d: "List[int]", c: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    d = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        d[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(M, d, c)


if __name__ == "__main__":
    main()
