#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(K: int, S: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(K, S)


if __name__ == "__main__":
    main()
