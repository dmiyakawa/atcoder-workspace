#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "YES"  # type: str
NO = "NO"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    s_r = int(next(tokens))  # type: int
    s_c = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(H, W, N, s_r, s_c, S, T)


def solve(H: int, W: int, N: int, s_r: int, s_c: int, S: str, T: str):
    return


if __name__ == "__main__":
    main()
