#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


# https://qiita.com/derodero24/items/91b6468e66923a87f39f
def cmb(n, r):
    """nCr を計算する。 factorial(N) // factorial(N - r) // factorial(r) より概して高速"""
    from operator import mul
    from functools import reduce
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def factorize_in_prime(n) -> "Dict[int, int]":
    """\
    2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す
    nが想定外の値の場合はAssertionErrorを送出する点に注意
    """
    assert isinstance(n, int) and n >= 2
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


def main():
    N, M = [int(e) for e in input().split()]
    print(solve(N, M))


def solve(N: int, M: int):
    if M == 1:
        return 1
    d = factorize_in_prime(M)
    count = 1
    for value in d.values():
        # Nから重複を許してvalue個選ぶ重複組合せ
        count = count * (cmb(N + value - 1, value) % MOD) % MOD
    return count


if __name__ == "__main__":
    main()
