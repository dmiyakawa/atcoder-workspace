#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, D: "List[int]", S: "List[int]", T: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [int()] * (N)  # type: "List[int]"
    S = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        D[i] = int(next(tokens))
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(N, D, S, T)


if __name__ == "__main__":
    main()
