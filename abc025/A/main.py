#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(S: str, N: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    N = int(next(tokens))  # type: int
    solve(S, N)


if __name__ == "__main__":
    main()
