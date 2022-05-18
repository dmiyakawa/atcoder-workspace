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
    S = next(tokens)  # type: str
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(S, a, b)


def solve(S: str, a: int, b: int):
    return


if __name__ == "__main__":
    main()
