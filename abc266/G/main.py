#!/usr/bin/env python3

MOD = 998244353  # type: int


def solve_ref(R: int, G: int, B: int, K: int):
    """https://atcoder.jp/contests/abc266/editorial/4669 の [2] 組み合わせ的解釈による解法"""
    fc = Factorial(MOD)
    Rk = R - K
    Gk = G - K

    # K, Gk, Bの組み合わせ
    a = fc.F(K + Gk + B)
    a *= fc._fact_inv(K)
    a %= MOD
    a *= fc._fact_inv(Gk)
    a %= MOD
    a *= fc._fact_inv(B)
    a %= MOD

    # 余ったRをGの左隣以外に置く。
    # Rの隣、Bの隣に加えて任意の列の右端もRを改めて置く候補になる
    # K + B + 1個から重複（Rを複数そこに置く）を許してRk個置く「重複組み合わせ」
    a *= fc.CWithReplacement(K + B + 1, Rk)
    a %= MOD
    print(a)


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


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve_ref(R, G, B, K)


if __name__ == "__main__":
    main()
