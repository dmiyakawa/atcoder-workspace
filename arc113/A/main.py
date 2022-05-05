#!/usr/bin/env python3

from functools import lru_cache
from math import sqrt
import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def factorize_in_prime(n):
    """\
    2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す
    prime_onlyがTrueのとき、素因数分解する
    """
    assert n >= 2
    d = {}
    temp = n
    for i in range(2, int(sqrt(n)) + 1):
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


@lru_cache(2 * (10 ** 5))
def calc(k):
    if k == 1:
        return 1
    factorized = factorize_in_prime(k)
    # print(f"{k} -> {factorized}")
    calc_k1 = calc(k - 1)
    tmp = 1
    for n in factorized.values():
        tmp = tmp * sum(1 for p in range(n + 1) for q in range(n - p + 1))

    # print(f"calc({k}) -> {tmp + calc_k1}")
    return tmp + calc_k1


def main():
    K = int(input())
    for k in range(1, K + 1):
        calc(k)
    print(calc(K))


if __name__ == "__main__":
    main()
