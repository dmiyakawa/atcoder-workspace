#!/usr/bin/env python3

import bisect
import typing

def main():
    N, K = map(int, input().split())
    A = [int(e) for e in input().split()]
    solve_ref(N, K, A)
    # solve(N, K, A)


def solve_ref(N, K, A):
    """https://atcoder.jp/contests/arc138/submissions/33415823"""
    p = [(A[i], i) for i in range(N)]
    p.sort(key=lambda tup: (tup[0], -tup[1]))

    ans = 10 ** 10
    # (K-1)以下インデックス番号のうち、最も大きいもの
    index_max = -1
    for Ai, index in p:
        # インデックス番号がK以上, かつ, (K-1)以下番目にAiより小さい値がある場合
        if K <= index and index_max != -1:
            # 入れ替えの操作回数=(index - index_max)
            # 大きければ答えを更新
            ans = min((index - index_max), ans)
        elif index < K:
            # 番号が大きければ更新
            index_max = max(index, index_max)

    print(-1 if ans == 10 ** 10 else ans)



def solve(N, K, A):
    """初AC。あまりにも回りくどい……"""
    B = [(a, i) for i, a in enumerate(A)]
    Bl = sorted(B[:K])
    Br = sorted(B[K:])
    Cl = [tup[0] for tup in Bl]
    Cr = [tup[0] for tup in Br]
    st_l = SegTree(op=max, e=0, v=[tup[1] for tup in Bl])
    st_r = SegTree(op=min, e=N, v=[tup[1] for tup in Br])
    min_ops = float("inf")

    for i in range(K - 1, -1, -1):
        j = bisect.bisect_right(Cr, A[i])
        if j < len(Cr):
            min_ops = min(min_ops, st_r.prod(j, len(Br)) - i)
    for i in range(K, N):
        j = bisect.bisect_left(Cl, A[i])
        if j > 0:
            min_ops = min(min_ops, i - st_l.prod(0, j))
    print(-1 if min_ops == float("inf") else min_ops)


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



if __name__ == "__main__":
    main()
