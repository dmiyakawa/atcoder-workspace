#!/usr/bin/env python3
from typing import List

MOD = 998244353  # type: int


def solve(N: int, M: int, K: int):
    if M == 1:
        print(1 if N <= K else 0)
        return

    f = Factorial(mod=MOD)
    inv_m = f.calc_modinv(M)
    # inv_m = 1 / M

    # dp[k][n] ... 残k回で残nマス
    dp: List[List[float]] = [[0] * (N + 1) for _ in range(K + 1)]
    # 1 <= K <= 1000
    for k in range(K + 1):
        dp[k][0] = 1
        if k == 0:
            continue
        # 1 <= M <= 10
        for m in range(1, M + 1):
            tmp = 1 * inv_m  # 一発でゴール
            for m1 in range(m - 1, 0, -1):
                tmp += 1 * inv_m * dp[k - 1][m1]
                tmp %= MOD
            for m2 in range(1, M - m + 1):
                tmp += 1 * inv_m * dp[k - 1][m2]
                tmp %= MOD
            dp[k][m] = tmp
            dp[k][m] %= MOD
        # M + 1 <= N <= 1000
        for n in range(M + 1, N + 1):
            tmp = 0
            for dice in range(1, M + 1):
                tmp += 1 * inv_m * dp[k - 1][n - dice]
                tmp %= MOD
            dp[k][n] = tmp
            dp[k][n] %= MOD
    print(dp[K][N] % MOD)


class Factorial:
    def __init__(self, mod: int):
        self._mod = mod
        self._fac = [1]
        self._size = 1
        self._iFac = [1]
        self._iSize = 1

    @staticmethod
    def xgcd(a: int, b: int) -> "Tuple[int, int, int]":
        """Returns (g, x, y) such that a*x + b*y = g = gcd(a, b);"""
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

    def H(self, n: int, k: int) -> int:
        """nHk % mod
        重複組合せ、つまり「n種類から重複を許してk個選ぶ」
        """
        t = self._fact_inv(n - 1) * self._fact_inv(k) % self._mod
        return self(n + k - 1) * t % self._mod

    CWithReplacement = H

    def put(self, n: int, k: int) -> int:
        return self.C(n + k - 1, k - 1)

    def pow(self, a, b):
        # Pythonの組み込み関数を使っているだけ。わざわざ実装してあるのは物忘れ対策
        return pow(a, b, self._mod)

    def _fact_inv(self, n: int) -> int:
        """1/n! % mod を返す"""
        if n >= self._mod:
            raise ValueError("Modinv does not exist. arg={}".format(n))
        self._make_inv(n)
        return self._iFac[n]

    def calc_modinv(self, n: int) -> int:
        """\
        mod p 上のnの逆元、つまり nx ≡ 1 (mod p) となるxを返す
        この関数は計算結果をオブジェクトにキャッシュしない
        """
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
                self._iFac.append(self.calc_modinv(self._fac[i]))
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
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, M, K)


if __name__ == "__main__":
    main()
