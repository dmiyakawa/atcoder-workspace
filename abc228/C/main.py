#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [[int(next(tokens)) for _ in range(3)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, K, P)


def solve(N: int, K: int, P: "List[List[int]]"):
    return


if __name__ == "__main__":
    main()
