#!/usr/bin/env python3

import sys
from typing import Dict

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, K, A, B)


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]"):
    a_i, b_i = 0, 0





if __name__ == "__main__":
    main()
