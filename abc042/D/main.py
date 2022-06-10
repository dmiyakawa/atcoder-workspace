#!/usr/bin/env python3

import sys
from functools import lru_cache

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def main():
    #
    # まだむーりー（2022-06-08）
    #
    H, W, A, B = [int(e) for e in input().split()]
    count = 1
    f_cache = {0: 1}
    for n in range(1, max(H, W) * 2 + 1):
        count = count * n
        f_cache[n] = count

    def factorial(n_):
        return f_cache[n_]

    @lru_cache(maxsize=-1)
    def cmb(n_, r_):
        return factorial(n_) // factorial(n_ - r_) // factorial(r_)

    lst1 = [cmb(H - A - 1 + i, H - A - 1) % MOD for i in range(B, W + 1)]
    lst2 = [cmb(A + i - 1, A - 1) % MOD for i in range(W - B - 1, -1, -1)]

    print(sum(a * b % MOD for a, b in zip(lst1, lst2)) % MOD)


if __name__ == "__main__":
    main()
