#!/usr/bin/env python3

from functools import lru_cache
import sys

sys.setrecursionlimit(2 * (10 ** 5))

MOD = 1000000007  # type: int

cache = {}


def calc_count(n, depth=0):
    if n in cache:
        return cache[n]
    count = 0
    # for i in range(min(n, 9), 0, -1):
    for i in range(1, min(n, 9) + 1):
        if n - i == 0:
            count = (count + 1) % MOD
        else:
            c = calc_count(n - i, depth + 1)
            count = (count + c) % MOD
    cache[n] = count
    return count


def main():
    K = int(input())
    if K % 9 != 0:
        print(0)
    else:
        print(calc_count(K))


if __name__ == "__main__":
    main()
