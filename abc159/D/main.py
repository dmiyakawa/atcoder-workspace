#!/usr/bin/env python3
from collections import Counter

def solve_3(N: int, A: "List[int]"):
    counter = Counter(A)
    total = 0
    for k, num in counter.items():
        if num >= 2:
            total += num*(num - 1) // 2
    for a in A:
        num = counter[a]
        print(total - num*(num - 1) // 2 + (num - 1)*(num -2)//2)


def solve_2(N: int, A: "List[int]"):
    counter = Counter(A)
    total = 0
    for k, num in counter.items():
        if num >= 2:
            total += comb(num, 2)
    for a in A:
        num = counter[a]
        x = comb(num, 2) if num >= 2 else 0
        y = comb(num - 1, 2) if num > 2 else 0
        print(total - x + y)


def solve(N: int, A: "List[int]"):
    counter = Counter(A)
    total = 0
    cache_1 = [0] * (N + 1)
    cache_2 = [0] * (N + 1)
    for k, num in counter.items():
        if num >= 2:
            cache_1[k] = comb(num, 2)
            total += cache_1[k]
        if num > 2:
            cache_2[k] = comb(num - 1, 2)
    for a in A:
        print(total - cache_1[a] + cache_2[a])


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


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_3(N, A)


if __name__ == "__main__":
    main()
