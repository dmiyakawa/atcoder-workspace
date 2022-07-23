#!/usr/bin/env python3
from collections import Counter

def main_mod():
    N = int(input())
    counter = sum((Counter(factorize_in_prime(n)) for n in range(2, N + 1)), Counter())
    ans = 0
    # 75
    for k1, v1 in counter.items():
        if v1 >= 74:
            ans += 1

    # 25, 3
    for k1, v1 in counter.items():
        if v1 < 24:
            continue
        for k2, v2 in counter.items():
            if v2 < 2:
                continue
            if k1 != k2:
                ans += 1

    # 15, 5
    for k1, v1 in counter.items():
        if v1 < 14:
            continue
        for k2, v2 in counter.items():
            if v2 < 4:
                continue
            if k1 != k2:
                ans += 1

    # 5, 5, 3
    for k1, v1 in counter.items():
        if v1 < 4:
            continue
        for k2, v2 in counter.items():
            if k1 > k2:
                continue
            if v2 < 4:
                continue
            for k3, v3 in counter.items():
                if v3 < 2:
                    continue
                if k1 != k2 and k2 != k3 and k3 != k1:
                    ans += 1
    print(ans)


def main():
    N = int(input())
    counter = sum((Counter(factorize_in_prime(n)) for n in range(2, N + 1)), Counter())
    a = {key for key, value in counter.items() if value >= 2}
    b = {key for key, value in counter.items() if value >= 4}
    c = {key for key, value in counter.items() if value >= 14}
    d = {key for key, value in counter.items() if value >= 24}
    e = {key for key, value in counter.items() if value >= 74}
    # print(counter)
    # print(2, sorted(a))
    # print(4, sorted(b))
    # print(14, sorted(c))
    # print(24, sorted(d))
    # print(74, sorted(e))

    lst = []

    # 3, 5, 5
    lst.append(len(a - b) * comb(len(b), 2) if len(b) >= 2 else 0)
    lst.append((comb(len(b), 3) * 3) if len(b) >= 3 else 0)

    # 5, 15
    lst.append(len(b - c) * len(c))
    lst.append((len(c) * (len(c) - 1)) if len(c) >= 2 else 0)

    # 3, 25
    lst.append(len(a - d) * len(d))
    lst.append((len(d) * (len(d) - 1)) if len(d) >= 2 else 0)

    lst.append(len(e))

    print(sum(lst))


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


if __name__ == "__main__":
    main_mod()
