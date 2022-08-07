#!/usr/bin/env python3

import sys
from typing import Union, Any, List

MOD = 998244353  # type: int


def solve_ref(N: int, A: "List[int]"):
    """\
    - https://atcoder.jp/contests/abc263/editorial/4546
    - https://atcoder.jp/contests/abc263/submissions/33857814
    - mod付き割り算が前提。フェルマーの小定理ベースの実装として割り算を掛け算に変換するのを忘れない
    - 無限等比級数の公式のひとつとして r + 2*r^2 + 3*r^3 + ... = r / (1 - r)^2 (https://mathwords.net/mugenwa 等)
    - 上記よりXつまり「サイコロで0を出す回数の期待値」がもとまる。ちなみに確率aの事象が起こるまでの総回数の期待値はそもそも1/aでおなじ。
    - A[i] が大きい場合に O(N^2) になるため、sum() 部分は工夫する。以下の実装ではseg木
    """
    mc = ModComb(1, p=MOD)
    ss = SegTree(op=lambda a, b: a + b, e=0, v=N)
    for i in range(N - 2, -1, -1):
        v = (ss.prod(i + 1, i + A[i] + 1) * mc.inverse(A[i]) + mc.inverse(A[i]) + 1) % MOD
        ss.set(i, v)
    print(ss.get(0) % MOD)


class SegTree:
    def __init__(
        self,
        op: "Callable[[Any, Any], Any]",
        e: "Any",
        v: "Union[int, List[Any]]",
    ) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self.__class__._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    @staticmethod
    def _ceil_pow2(n: int) -> int:
        x = 0
        while (1 << x) < n:
            x += 1
        return x

    def set(self, p: int, x: "Any") -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> "Any":
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> "Any":
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> "Any":
        return self._d[1]

    def max_right(self, left: int, f: "Callable[[Any], bool]") -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: "Callable[[Any], bool]") -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


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
    A = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve_ref(N, A)


if __name__ == "__main__":
    main()
