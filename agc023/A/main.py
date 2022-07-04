#!/usr/bin/env python3

import sys
from collections import Counter


def comb(n, r):
    """nCr を計算する。 factorial(N) // factorial(N - r) // factorial(r) より概して高速"""
    from operator import mul
    from functools import reduce
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def solve(N: int, A: "List[int]"):
    S = [0 for _ in range(N + 1)]
    for i, a in enumerate(A, start=1):
        S[i] = S[i - 1] + a
    c = Counter(S)
    count = 0
    for value in c.values():
        if value > 1:
            count += comb(value, 2)
    print(count)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
