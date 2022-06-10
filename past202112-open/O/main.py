#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int, B: "List[int]", S: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, B, S)


if __name__ == "__main__":
    main()
