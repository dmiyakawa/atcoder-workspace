#!/usr/bin/env python3

MOD = 1000000007


class ModComb:
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

    def C(self, n, r) -> int:
        """nCr mod p を求める"""
        if n < r:
            return 0
        a = self.factorial(n)
        b = self.factorial(n - r)
        c = self.factorial(r)
        bc = (b * c) % self._p
        return a * self.inverse(bc) % self._p


def solve(X, Y):
    if (X + Y) % 3 != 0:
        return 0
    n = (X + Y) // 3
    if X < n or Y < n:
        return 0
    md = ModComb(N=2 * 10 ** 6, p=MOD)
    k = X - n
    return md.C(n, k)


def main():
    X, Y = map(int, input().split())
    print(solve(X, Y))


if __name__ == "__main__":
    main()
