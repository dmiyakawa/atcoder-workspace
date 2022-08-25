#!/usr/bin/env python3


MOD = 998244353  # type: int


def solve_ref(N: int, A: "List[List[int]]"):
    """https://atcoder.jp/contests/abc259/editorial/4269"""
    # 遅い
    # mc = ModComb(N**2, p=MOD)
    F = Factorial(MOD)
    d = {}
    for h in range(N):
        for w in range(N):
            c = A[h][w]
            d.setdefault(c, []).append((h, w))
    count = 0
    for c, cells in d.items():
        if len(cells) <= N:
            for i, (h0, w0) in enumerate(cells):
                for h1, w1 in cells[i:]:
                    h2, w2 = h1 - h0, w1 - w0
                    if h2 * w2 < 0:
                        continue
                    elif h2 * w2 == 0:
                        count = (count + 1) % MOD
                    else:
                        h2, w2 = abs(h2), abs(w2)
                        count = (count + F.C(h2 + w2, h2)) % MOD
        else:
            # とんでもなく遅い (pypyでも)
            # dp = [[(1 if (h, w) in cells else 0) for h in range(N)] for w in range(N)]

            dp = [[0] * N for _ in range(N)]
            for h, w in cells:
                dp[h][w] = 1
            for h in range(N):
                for w in range(N):
                    if h > 0:
                        dp[h][w] += dp[h-1][w]
                    if w > 0:
                        dp[h][w] += dp[h][w - 1]
                    dp[h][w] %= MOD
            for h, w in cells:
                count = (count + dp[h][w]) % MOD

            # これだとTLE
            # dp = [0 for _ in range(N**2)]
            # for i in range(N**2):
            #     h, w = divmod(i, N)
            #     ca = A[h][w]
            #     top = dp[(h-1)*N + w] if h > 0 else 0
            #     left = dp[h*N + w - 1] if w > 0 else 0
            #     dp[i] = (top + left + (1 if c == ca else 0)) % MOD
            #     # if c == ca:
            #     #     count = (count + dp[i]) % MOD
            #
            # for h, w in cells:
            #     count = (count + dp[h*N] + w) % MOD

    print(count % MOD)


class Factorial:
    # https://atcoder.jp/contests/abc259/submissions/33770080
    def __init__(self, mod: int):
        self._mod = mod
        self._fac = [1]
        self._size = 1
        self._iFac = [1]
        self._iSize = 1

    @staticmethod
    def xgcd(a: int, b: int):
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def F(self, n: int) -> int:
        if n >= self._mod:
            return 0
        self._make(n)
        return self._fac[n]

    def C(self, n: int, k: int) -> int:
        if n < 0 or k < 0 or n < k:
            return 0
        t = self._fact_inv(n - k) * self._fact_inv(k) % self._mod
        return self(n) * t % self._mod

    def _fact_inv(self, n: int) -> int:
        """n!^-1 % mod"""
        if n >= self._mod:
            raise ValueError("Modinv is not exist! arg={}".format(n))
        self._make_inv(n)
        return self._iFac[n]

    def _modinv(self, n: int) -> int:
        gcd_, x, _ = self.xgcd(n, self._mod)
        if gcd_ != 1:
            raise ValueError("Modinv is not exist! arg={}".format(n))
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


class ModComb:
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

    def C(self, n, r) -> int:
        """nCr mod p を求める"""
        if n < r:
            return 0
        a = self.factorial(n)
        b = self.factorial(n - r)
        c = self.factorial(r)
        bc = (b * c) % self._p
        return a * self.inverse(bc) % self._p


def main():
    N = int(input())
    A = [[int(e) for e in input().split()] for _ in range(N)]
    solve_ref(N, A)


def _debug(N=400):
    A = [[1 for _ in range(N)] for _ in range(N)]
    solve_ref(N, A)


def _debug2(N=400):
    A = [[h*w for w in range(1, N+1)] for h in range(1, N+1)]
    solve_ref(N, A)


if __name__ == "__main__":
    # _debug()
    main()

