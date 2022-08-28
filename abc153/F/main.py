#!/usr/bin/env python3
import bisect


def solve(N: int, D: int, A: int, X: "List[int]", H: "List[int]"):
    max_H = max(H)
    XH = sorted((x, h) for x, h in zip(X, H))
    X = [x for x, h in XH]

    def _composition(f, g):
        return lambda x: f(g(x))

    def _op(x, y):
        lst = [(max_H, N)]
        if x[0] > 0:
            lst.append(x)
        if y[0] > 0:
            lst.append(y)
        return sorted(lst)[0]

    st = LazySegTree(op=_op,
                     e=(max_H, len(H)),
                     mapping=lambda f, x: (f(x[0]), x[1]),
                     composition=_composition,
                     id_=lambda x: x,
                     v=[(h, i) for i, (x, h) in enumerate(XH)])

    ans = 0
    i = 0
    h = H[0]
    while i < N:
        assert h > 0
        x = X[i]
        j = bisect.bisect(X, x + 2 * D)
        ac = h // A + (1 if h % A else 0)
        st.apply(i, j, f=lambda x: x - A * ac)
        ans += ac
        h, i = st.all_prod()
        # print(f"i: {i}, x: {x}, h: {h}, ac: {ac}, ans: {ans}, next_i: {next_i}")

    print(ans)



class LazySegTree:
    def __init__(
        self,
        op: "Callable[[Any, Any], Any]",
        e: "Any",
        mapping: "Callable[[Any, Any], Any]",
        composition: "Callable[[Any, Any], Any]",
        id_: "Any",
        v: "Union[int, List[Any]]",
    ) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self.__class__._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
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
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> "Any":
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> "Any":
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
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

    def apply(
        self,
        left: int,
        right: "Optional[int]" = None,
        f: "Optional[Any]" = None,
    ) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left: int, g: "Callable[[Any], bool]") -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: "Any") -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: "Any") -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id




def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    H = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        H[i] = int(next(tokens))
    solve(N, D, A, X, H)


if __name__ == "__main__":
    main()