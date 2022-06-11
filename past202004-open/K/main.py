#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, S: str, C: "List[int]", D: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, C, D)


if __name__ == "__main__":
    main()
