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
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F, X)


def solve(A: int, B: int, C: int, D: int, E: int, F: int, X: int):
    x = X
    takahashi_m = 0
    aoki_m = 0
    while x > 0:
        to_run = min(x, A)
        takahashi_m += to_run * B
        to_wait = min(x, C)
        x -= to_run + to_wait
    x = X
    while x > 0:
        to_run = min(x, D)
        aoki_m += to_run * E
        to_wait = min(x, F)
        x -= to_run + to_wait

    if takahashi_m > aoki_m:
        print("Takahashi")
    elif takahashi_m < aoki_m:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
