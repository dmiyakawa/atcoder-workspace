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
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    F = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A, F)


def solve(N: int, K: int, A: "List[int]", F: "List[int]"):
    return


if __name__ == "__main__":
    main()
