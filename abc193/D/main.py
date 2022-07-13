#!/usr/bin/env python3

from collections import Counter


def main():
    K, S, T = int(input()), input(), input()
    s_d = [int(ch) for ch in S[:-1]]
    t_d = [int(ch) for ch in T[:-1]]

    rem = {n: K for n in range(1, 10)}
    for n in s_d + t_d:
        rem[n] -= 1
    ans = 0
    for a in range(1, 10):
        for b in range(1, 10):
            if (a == b and rem[a] < 2) or rem[a] < 1 or rem[b] < 1:
                continue
            taka_c = Counter(s_d + [a])
            aoki_c = Counter(t_d + [b])
            taka_sc = sum(k * 10 ** taka_c.get(k, 0) for k in range(1, 10))
            aoki_sc = sum(k * 10 ** aoki_c.get(k, 0) for k in range(1, 10))
            if taka_sc <= aoki_sc:
                continue
            res_sum = sum(rem.values())
            if a == b:
                p = rem[a] * (rem[a] - 1) / (res_sum * (res_sum - 1))
            else:
                p = rem[a] * rem[b] / (res_sum * (res_sum - 1))
            ans += p
    print(ans)


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
    main()
