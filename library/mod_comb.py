#!/usr/bin/env python3
#
# https://yukicoder.me/problems/no/117
#

import unittest


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
        self._factorial_cache = [1 for _ in range(N + 1)]
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
    import re
    import sys
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        T = int(input())
        args = [input() for _ in range(T)]
    mc = ModComb(2 * 10 ** 6)
    for arg in args:
        m = re.match(r"([CPH])\((\d+)\s*,\s*(\d+)\)", arg)
        if m:
            n, r = int(m.group(2)), int(m.group(3))
            if m.group(1) == "P":
                print(mc.P(n, r))
                continue
            elif m.group(1) == "C":
                print(mc.C(n, r))
                continue
            elif m.group(1) == "H":
                print(mc.H(n, r))
                continue
        raise RuntimeError(f"Unknown format \"{arg}\"")


if __name__ == "__main__":
    main()


class ModCombTest(unittest.TestCase):
    def test_1(self):
        mc = ModComb(2 * 10**6)
        self.assertEqual(60, mc.P(5, 3))
        self.assertEqual(6, mc.C(4, 2))
        self.assertEqual(1, mc.C(0, 0))
        self.assertEqual(1, mc.C(1, 0))
        self.assertEqual(1, mc.H(1, 0))
        self.assertEqual(1, mc.H(0, 0))
        self.assertEqual(0, mc.P(1, 10))
        self.assertEqual(872804403, mc.P(702335, 182588))
        self.assertEqual(791955010, mc.C(710592, 306554))
