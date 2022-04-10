#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [str()] * (M)  # type: "List[str]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        S[i] = next(tokens)
        C[i] = int(next(tokens))
    solve(N, M, S, C)


def solve(N: int, M: int, S: "List[str]", C: "List[int]"):
    return


if __name__ == "__main__":
    main()
