#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, P: "List[int]", V: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N - 2 + 1)]  # type: "List[int]"
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, V)


if __name__ == "__main__":
    main()
