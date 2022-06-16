#!/usr/bin/env python3
from collections import Counter


def comb(n, r):
    """nCr を計算する。 factorial(N) // factorial(N - r) // factorial(r) より概して高速"""
    if n < r:
        return 0
    from operator import mul
    from functools import reduce
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    input()
    c = Counter(int(e) for e in input().split())
    print(comb(c[1], 2) + comb(c[2], 2) + comb(c[3], 2))


if __name__ == "__main__":
    main()
