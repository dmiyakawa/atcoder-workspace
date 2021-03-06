#!/usr/bin/env python3

import math
import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def solve(N: int):
    mc = ModComb(N**2, p=MOD)
    count = 0
    for n in range(N, N**2 - N + 2):
        count = (count + mc.C(n - 1, N - 1) * (mc.C(N**2 - n, N - 1) * mc.factorial((N - 1)**2 % MOD))) % MOD
    count = (count * ((math.factorial(N) % MOD) ** 2)) % MOD
    print((mc.factorial(N**2) % MOD - count) % MOD)


class ModComb:
    """\
    N! mod p 、またそれを前提とした nCr, nPr, nHr の計算を前処理付きで高速に計算する
    nHr = (n+r-1)Cr であるため、重複組合せを求める際にはNの数値を2倍程度にする必要がある可能性に注意
    """
    def __init__(self, N, p: int = 1_000_000_007):
        """\
        :param N: 乗数の最大値。
        :param p: 剰余に用いる数。このクラスが正しく機能するためには素数である必要がある
        """
        self._N = N
        self._p = p
        self._factorial_cache = {0: 1}
        for i in range(1, N + 1):
            self._factorial_cache[i] = (self._factorial_cache[i - 1] * i) % p

    def factorial(self, n):
        return self._factorial_cache[n]

    def inverse(self, x):
        """xの逆数 (mod p) を返す"""
        # フェルマーの小定理からxの逆数をx'とすると x' = x^(p-2) mod p
        k = self._p - 2
        ret = 1
        y = x
        while k:
            if k & 1:
                ret = (ret * y) % self._p
            y = (y * y) % self._p
            k //= 2
        return ret

    def P(self, n, r) -> int:
        """nPr mod p を求める"""
        if n < r:
            return 0
        a = self.factorial(n)
        b = self.factorial(n - r)
        return (a * self.inverse(b)) % self._p

    def C(self, n, r) -> int:
        """nCr mod p を求める"""
        if n < r:
            return 0
        a = self.factorial(n)
        b = self.factorial(n - r)
        c = self.factorial(r)
        bc = (b * c) % self._p
        return a * self.inverse(bc) % self._p

    def H(self, n, r) -> int:
        """\
        nHr mod p (重複組合せ) を求める
        """
        if r == 0:
            return 1
        return self.C(n + r - 1, r)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
