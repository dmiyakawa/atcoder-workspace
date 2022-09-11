#!/usr/bin/env python3

"""\
数論変換
"""


class NTT:
    """https://atcoder.jp/contests/practice2/submissions/33653363"""
    def __init__(self, mod):
        self.mod = mod
        return

    def _ntt(self, a, n, sig):
        mod = self.mod
        fa = a + [0] * (n - len(a))
        h = pow(3, (mod - 1) // n, mod)
        if sig < 0:
            h = pow(h, mod - 2, mod)
        i = 0
        m = n >> 1
        for j in range(1, n - 1):
            k = m
            i ^= k
            while i < k:
                k >>= 1
                i ^= k
            if j < i:
                fa[i], fa[j] = fa[j], fa[i]
        m = 1
        while m < n:
            m2 = m << 1
            base = pow(h, n // m2, mod)
            w = 1
            for x in range(m):
                for i in range(x, n, m2):
                    j = i + m
                    u = fa[i]
                    d = fa[j] * w
                    if d >= mod:
                        d %= mod
                    fai = u + d
                    if mod <= fai:
                        fai -= mod
                    fa[i] = fai
                    faj = u - d
                    if faj < 0:
                        faj += mod
                    fa[j] = faj
                w *= base
                if w >= base:
                    w %= mod
            m = m2

        for i in range(n):
            if fa[i] < 0:
                fa[i] += mod
        return fa

    def ntt(self, a, n):
        return self._ntt(a, n, 1)

    def intt(self, a, n):
        mod = self.mod
        res = self._ntt(a, n, -1)
        inv = pow(n, mod - 2, mod)
        return [ri * inv % mod for ri in res]

    def convolve(self, a, b):
        """畳み込みを(mod込で)行う"""
        mod = self.mod
        l = len(a) + len(b) - 1
        n = 1 << l.bit_length()
        A = self.ntt(a, n)
        B = self.ntt(b, n)
        F = [i * j % mod for i, j in zip(A, B)]
        f = self.intt(F, n)
        return f[:l]


def practice2_f():
    MOD = 998244353
    import sys
    input = sys.stdin.readline
    _, _ = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ntt = NTT(MOD)
    C = ntt.convolve(A, B)
    print(*C)


if __name__ == "__main__":
    practice2_f()
