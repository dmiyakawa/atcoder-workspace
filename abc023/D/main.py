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
    H = [int()] * (N)  # type: "List[int]"
    S = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        H[i] = int(next(tokens))
        S[i] = int(next(tokens))
    solve(N, H, S)


def solve(N: int, H: "List[int]", S: "List[int]"):
    return


if __name__ == "__main__":
    main()
