#!/usr/bin/env python3

import sys
from typing import List, Optional

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, C: int, T: "List[int]", A: "List[int]"):
    conv: List[List[List[Optional[int]]]] = [[[None for _ in range(N)] for _ in range(30)] for _ in range(2)]
    for b in range(2):
        for i in range(30):
            for j in range(N):
                t, a = T[j], A[j]
                val = b if j == 0 else conv[b][i][j - 1]
                rel_b = (a >> i & 1)
                if t == 1:  # and
                    new_val = val & rel_b
                elif t == 2:  # or
                    new_val = val | rel_b
                else:  # xor
                    new_val = val ^ rel_b
                conv[b][i][j] = new_val
    c = C
    for j in range(N):
        new_c = 0
        for i in range(30):
            rel_b = (c >> i & 1)
            new_c |= (conv[rel_b][i][j] << i)
        print(new_c)
        c = new_c


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, C, T, A)


if __name__ == "__main__":
    main()
