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


def split3(prime, num):
    lst = []
    for i in range(num + 1):
        for j in range(i, num + 1):
            lst.append((prime ** i, prime ** (j - i), prime ** (num - j)))
    return lst


def main():
    K = int(input())
    print(solve(K))


def solve(K):
    if K == 1:
        return 1

    f = factorize_in_prime(K)
    lst = [split3(key, value) for key, value in f.items()]
    count = 0
    for a, b, c in accum(lst):
        if a <= b <= c:
            count += 1
    return count


def accum(lst):
    for a, b, c in lst[0]:
        if lst[1:]:
            for ret in accum(lst[1:]):
                yield a * ret[0], b * ret[1], c * ret[2]
        else:
            yield a, b, c


if __name__ == "__main__":
    main()
