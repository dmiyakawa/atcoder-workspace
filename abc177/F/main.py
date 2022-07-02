#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(H: int, W: int, A: "List[int]", B: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int()] * (H)  # type: "List[int]"
    B = [int()] * (H)  # type: "List[int]"
    for i in range(H):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(H, W, A, B)


if __name__ == "__main__":
    main()
