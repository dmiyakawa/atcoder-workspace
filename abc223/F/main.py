#!/usr/bin/env python3

import typing


class SegTree:
    def __init__(
        self,
        op: typing.Callable[[typing.Any, typing.Any], typing.Any],
        e: typing.Any,
        v: typing.Union[int, typing.List[typing.Any]],
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

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
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

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int, f: typing.Callable[[typing.Any], bool]) -> int:
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

    def min_left(self, right: int, f: typing.Callable[[typing.Any], bool]) -> int:
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

def solve_ans(N, S, queries):
    # https://atcoder.jp/contests/abc223/editorial/2774
    # ( で +1, ) で -1 となる数列 A = (A1, ..., AM) と
    # Aの前からの累積和を取った数列 B = (B1, ..., BM) を考える
    # Sが正しい括弧列であるとは、BM が 0 かつ min(B) が 0 であるということ
    # - BM がではないと (と)の対応関係がどこかで取れていない
    # - min(B)が0より小さいと、途中で)が(より多くなっており、括弧の対応関係がおかしくなっている
    v = []
    for i, ch in enumerate(S):
        if ch == "(":
            v.append((0, 1))
        else:
            v.append((-1, -1))

    def _op(a, b):
        return min(a[0], a[1] + b[0]), a[1] + b[1]

    seg = SegTree(op=_op, e=(0, 0), v=v)
    for t, l, r in queries:
        l, r = l - 1, r - 1
        if t == 1:
            v[l], v[r] = v[r], v[l]
            seg.set(l, v[l])
            seg.set(r, v[r])
        else:
            if seg.prod(l, r + 1) == (0, 0):
                print("Yes")
            else:
                print("No")


def main():
    N, Q = map(int, input().split())
    S = input()
    queries = []
    for _ in range(Q):
        queries.append(tuple(int(e) for e in input().split()))
    solve_ans(N, S, queries)


if __name__ == "__main__":
    main()
