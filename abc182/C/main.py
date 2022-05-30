#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    N = int(input())
    print(solve(N))


def solve(N: int):
    ns = str(N)
    min_digits = Inf
    for i in range(2**len(ns)):
        s = "".join(ch for j, ch in enumerate(ns) if 2**j & i)
        val = int(s) if len(s) > 0 else 0
        if val > 0 and val % 3 == 0:
            min_digits = min(len(ns) - len(s), min_digits)
    return -1 if min_digits is Inf else min_digits


if __name__ == "__main__":
    # import random
    # for i in range(10000):
    #     N = random.randrange(10**17, 10**18)
    #     print(i, N, solve(N))
    main()
