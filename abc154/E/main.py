#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: str, K: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == "__main__":
    main()
