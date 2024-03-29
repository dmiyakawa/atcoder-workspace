#!/usr/bin/env python3

MOD = 10**9 + 7


def solve(R, C, X, Y, D, L) -> int:
    fc = Factorial(MOD)
    if X == 1 or Y == 1:
        # 2つの端に何かある
        v = fc.C(X * Y - 2, D + L - 2)
    else:
        # 4隅の状態を軸に16パターンを6通りに分解する。それぞれは互いに独立事象
        XY = X * Y
        M = D + L
        if M >= 4:
            # a: X, Yの4隅になにかある
            a = fc.C(XY - 4, M - 4)
        else:
            a = 0
        if M >= 3:
            # b: X, Y の4隅のうち3つになにかある
            b = fc.C(XY - 4, M - 3) * 4 % MOD
        else:
            b = 0
        if M >= 2:
            # c: X, Y の4隅のうち、対角に2つなにかある
            c = fc.C(XY - 4, M - 2) * 2 % MOD
        else:
            c = 0

        if M >= 2 and XY - 4 >= M - 2:
            # d: X, Y の4隅のうち、対角でない2つに何かある
            d = fc.C(XY - 4, M - 2) * 4
            d -= fc.C(X * (Y - 1) - 2, M - 2) * 2
            d -= fc.C((X - 1) * Y - 2, M - 2) * 2
            d %= MOD
        else:
            d = 0

        # e: X, Y の4隅のうち、1つに何かある
        if M >= 1 and XY - 4 >= M - 1:
            e = fc.C(XY - 4, M - 1) * 4
            e -= fc.C((X - 1) * (Y - 1) - 1, M - 1) * 4
            e %= MOD
        else:
            e = 0

        # f: X, Y の4隅のいずれにもなにもない
        f = 0
        if XY - 4 >= M:
            for le in range(1, X - 1):
                for re in range(1, X - 1):
                    for ue in range(1, Y - 1):
                        for de in range(1, Y - 1):
                            tmp = fc.C(X - 2, le)
                            tmp *= fc.C(X - 2, re)
                            tmp %= MOD
                            tmp *= fc.C(Y - 2, ue)
                            tmp %= MOD
                            tmp *= fc.C(Y - 2, de)
                            tmp %= MOD
                            tmp *= fc.C((X - 2) * (Y - 2), M - ue - de - le - re)
                            tmp %= MOD
                            f += tmp
                            f %= MOD

        v = a + b + c + d + e + f
        # print(a, b, c, d, e, f)
        v %= MOD

    v *= fc.C(D + L, D)
    v %= MOD
    v *= (R - X + 1)
    v %= MOD
    v *= (C - Y + 1)
    v %= MOD
    return v


def solve_part(R, C, X, Y, D, L) -> int:
    fc = Factorial(MOD)
    return fc.C(D + L, D) * (R - X + 1) * (C - Y + 1) % MOD


def main():
    (R, C), (X, Y), (D, L) = [map(int, input().split()) for _ in range(3)]
    # print(solve_part(R, C, X, Y, D, L))
    print(solve(R, C, X, Y, D, L))


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


if __name__ == "__main__":
    main()
