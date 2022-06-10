#!/usr/bin/env python3

import sys
from typing import List, Tuple

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, W: int, A: "List[int]", B: "List[int]"):
    lst: List[Tuple[int, int]] = sorted(zip(A, B), reverse=True)
    i = 0
    value = 0
    for i in range(N):
        amount = min(lst[i][1], W)
        value += amount * lst[i][0]
        W -= amount
        if W == 0:
            break
    print(value)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, W, A, B)


if __name__ == "__main__":
    main()
