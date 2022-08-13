#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, T: "List[str]", P: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [str()] * (N)  # type: "List[str]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = next(tokens)
        P[i] = int(next(tokens))
    solve(N, T, P)


if __name__ == "__main__":
    main()
