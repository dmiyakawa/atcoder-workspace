#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(L: int, R: int, A: "List[int]", B: "List[int]", C: "List[List[int]]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(L)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(R)]  # type: "List[int]"
    C = [[int(next(tokens)) for _ in range(R)] for _ in range(L)]  # type: "List[List[int]]"
    solve(L, R, A, B, C)


if __name__ == "__main__":
    main()
