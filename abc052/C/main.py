#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce

MOD = 10**9 + 7


def main():
    N = int(input())
    d_total = defaultdict(int)
    if N == 1:
        print(1)
        return

    for n in range(2, N + 1):
        d = factorize_in_prime(n)
        for k, v in d.items():
            d_total[k] += v
    print(reduce(lambda x, y: (x * y) % MOD, [v + 1 for v in d_total.values()]))


def factorize_in_prime(n) -> "Dict[int, int]":
    """2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す"""
    # https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
    assert n >= 2
    d = {}
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                count += 1
                temp //= i
            d[i] = count

    if temp != 1:
        d[temp] = 1

    if not d:
        d[n] = 1

    return d


if __name__ == "__main__":
    main()
