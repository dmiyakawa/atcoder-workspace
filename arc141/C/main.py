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
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, P, Q)


def solve(N: int, P: "List[int]", Q: "List[int]"):
    return


if __name__ == "__main__":
    main()
