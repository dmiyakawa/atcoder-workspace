#!/usr/bin/env python3

MOD = 1000000007


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


def solve(X, Y):
    if (X + Y) % 3 != 0:
        return 0
    n = (X + Y) // 3

    fmod_cache = [1]
    for i in range(n):
        fmod_cache.append((i * fmod_cache[-1]) % MOD)
    # フェルマーの小定理を利用して割り算部分を掛け算に変換する
    # x mod p (pは素数) 上では逆数x' = x^(p - 2)
    # p = 1000000007 なので x' = x^1000000005
    # 1 / factorial(r) = factorial(r)^1000000005 (mod p)
    # 繰り返し二乗法
    #

    if X < n or Y < n:
        return 0
    k = X - n
    print(X, Y, n, k)
    return comb(n, k)


def main():
    X, Y = map(int, input().split())
    print(solve(X, Y))


if __name__ == "__main__":
    main()
