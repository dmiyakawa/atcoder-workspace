#!/usr/bin/env python3
from math import factorial

MOD = 998244353  # type: int

def solve(N: int, M: int, A: int, B: int, C: int, D: int, E: int, F: int, X: "List[int]", Y: "List[int]"):
    fc = Factorial(MOD)
    num = 0
    ng = {(x, y) for x, y in zip(X, Y)}

    for i in range(N + 1):
        for j in range(N - i + 1):
            k = N - i - j
            num += fc.F(N) * fc._fact_inv(i) * fc._fact_inv(j) * fc._fact_inv(k)
            num %= MOD
            for k in range(N - i - j + 1):
                x = i * A + j * C + k * E
                y = i * B + j * D + k * F
                if (x, y) in ng:
                    M1 = i + j + k
                    M2 = N - M1


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




def solve_tle(N: int, M: int, A: int, B: int, C: int, D: int, E: int, F: int, X: "List[int]", Y: "List[int]"):
    dp = {(0, 0): 1}
    ng = {(x, y) for x, y in zip(X, Y)}
    for _ in range(N):
        next_dp = {}
        for (x, y), val in dp.items():
            for dx, dy in [(A, B), (C, D), (E, F)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in ng:
                    continue
                next_dp[(nx, ny)] = next_dp.get((nx, ny), 0) + val
                next_dp[(nx, ny)] %= MOD
        dp = next_dp
    print(sum(dp.values()) % MOD)


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
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, A, B, C, D, E, F, X, Y)


if __name__ == "__main__":
    main()
