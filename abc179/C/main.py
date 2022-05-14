#!/usr/bin/env python3

from functools import lru_cache


def factorize_in_prime(n) -> "Dict[int, int]":
    """2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す"""
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


@lru_cache(10**6)
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


def main():
    N = int(input())
    print(solve(N))


def solve_slow(N) -> int:
    dp = {2: 1}

    for n in range(3, N + 1):
        primes = factorize_in_prime(n - 1)
        count = 1
        for value in primes.values():
            count *= value + 1
        count += dp[n - 1]
        dp[n] = count
    return dp[N]


def solve(N) -> int:
    count = 0
    for a in range(1, N):
        b = int((N - 1) / a)
        mul = a * b
        if mul < N:
            # print(f"A * B < N ... {a} * {b} < {N}")
            count += b
    return count


if __name__ == "__main__":
    main()
