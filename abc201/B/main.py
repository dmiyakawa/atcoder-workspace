#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, S: "List[str]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    T = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        T[i] = int(next(tokens))
    solve(N, S, T)


if __name__ == "__main__":
    main()
