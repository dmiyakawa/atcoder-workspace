#!/usr/bin/env python3

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


def solve(N) -> int:
    if N == 1:
        return 1
    d = factorize_in_prime(N)
    count = 1
    print(d)
    for key, value in d.items():
        # nHn
        count *= comb(value + 2, value)
    return count


def main():
    N = int(input())
    print(solve(N))


if __name__ == "__main__":
    main()
