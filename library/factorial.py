from typing import Tuple


class Factorial:
    def __init__(self, mod: int):
        self._mod = mod
        self._fac = [1]
        self._size = 1
        self._iFac = [1]
        self._iSize = 1

    @staticmethod
    def xgcd(a: int, b: int) -> "Tuple[int, int, int]":
        """\
        Returns (g, x, y) such that a*x + b*y = g = gcd(a, b);
        """
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def F(self, n: int) -> int:
        """n! % mod; factorial"""
        if n >= self._mod:
            return 0
        self._make(n)
        return self._fac[n]

    def C(self, n: int, k: int) -> int:
        """nCk % mod; combination"""
        if n < 0 or k < 0 or n < k:
            return 0
        t = self._fact_inv(n - k) * self._fact_inv(k) % self._mod
        return self(n) * t % self._mod

    def A(self, n: int, k: int) -> int:
        """nPk % mod"""
        if n < 0 or k < 0 or n < k:
            return 0
        return self(n) * self._fact_inv(n - k) % self._mod

    def CWithReplacement(self, n: int, k: int) -> int:
        """nHk % mod"""
        t = self._fact_inv(n - 1) * self._fact_inv(k) % self._mod
        return self(n + k - 1) * t % self._mod

    def put(self, n: int, k: int) -> int:
        return self.C(n + k - 1, k - 1)

    def _fact_inv(self, n: int) -> int:
        if n >= self._mod:
            raise ValueError("Modinv does not exist. arg={}".format(n))
        self._make_inv(n)
        return self._iFac[n]

    def _modinv(self, n: int) -> int:
        # modinv(a)はax≡1(modp)となるxをreturnする。
        # ax≡y(modp)となるxは上のreturnのy倍
        gcd_, x, _ = self.xgcd(n, self._mod)
        if gcd_ != 1:
            raise ValueError("Modinv does not exist. arg={}".format(n))
        return x % self._mod

    def _make(self, n: int) -> None:
        if n >= self._mod:
            n = self._mod
        if self._size < n + 1:
            for i in range(self._size, n + 1):
                self._fac.append(self._fac[i - 1] * i % self._mod)
            self._size = n + 1

    def _make_inv(self, n: int) -> None:
        if n >= self._mod:
            n = self._mod
        self._make(n)
        if self._iSize < n + 1:
            for i in range(self._iSize, n + 1):
                self._iFac.append(self._modinv(self._fac[i]))
            self._iSize = n + 1

    def __call__(self, n: int) -> int:
        """n! % mod"""
        return self.F(n)
