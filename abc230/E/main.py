#!/usr/bin/env python3
import math
from functools import reduce
from itertools import product
from operator import mul

def solve_ref(N):
    """https://atcoder.jp/contests/abc230/editorial/3015"""
    k0 = int(math.sqrt(N))
    ans = 0
    for k in range(1, k0 + 1):
        ans += ((N // k) - (N // (k + 1))) * k

    for k in range(1, N // (k0 + 1) + 1):
        ans += N // k

    print(ans)


def solve_tle(N: int):
    """\
    TLE例: 260158260522
    """
    if N == 1:
        print(1)
        return
    d = factorize_in_prime(N)
    tmp = [[k ** i for i in range(v + 1)] for k, v in d.items()]
    lst = sorted(reduce(mul, p) for p in product(*tmp))
    ans = N
    # print(lst)
    for i in range(1, len(lst)):
        a0 = N // lst[i - 1]
        a1 = N // lst[i]
        # print(i, lst[i] - lst[i - 1], a0 - a1)
        if i == 1 or (lst[i] - lst[i - 1] < a0 - a1):
            for j in range(lst[i - 1] + 1, lst[i] + 1):
                ans += int(N / j)
        else:
            for a in range(a1, a0):
                ans += (int(N / a) - int(N / (a + 1))) * a


    print(ans)


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


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve_ref(N)





if __name__ == "__main__":
    main()
