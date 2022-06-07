#!/usr/bin/env python3

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


def main():
    from functools import reduce
    from itertools import product
    N = int(input())
    if N == 1:
        ans = {1}
    else:
        ans = set()
        d = factorize_in_prime(N)
        for comb in product(*[[key**i for i in range(value + 1)] for key, value in d.items()]):
            ans.add(reduce(lambda x, y: x * y, comb))

    for n in sorted(ans):
        print(n)


if __name__ == "__main__":
    main()
