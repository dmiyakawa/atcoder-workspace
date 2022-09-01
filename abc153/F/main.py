#!/usr/bin/env python3

import bisect
import math


def solve_2(N: int, D: int, A: int, X: "List[int]", H: "List[int]"):
    XH = sorted((x, h) for x, h in zip(X, H))
    X = [x for x, h in XH]
    H = [h for x, h in XH]
    C = [0] * N
    cur = 0
    ans = 0
    for i in range(N):
        cur += C[i]
        if H[i] - cur > 0:
            count = math.ceil((H[i] - cur) / A)
            cur += A * count
            ans += count
            j = bisect.bisect(X, X[i] + 2 * D)
            if j < N:
                C[j] -= A * count
    print(ans)


def solve(N: int, D: int, A: int, X: "List[int]", H: "List[int]"):
    max_H = max(H)
    XH = sorted((x, h) for x, h in zip(X, H))
    H = [h for x, h in XH]
    X = [x for x, h in XH]

    _e = max_H + 1

    def _mapping(f, x):
        return f(x)

    def _composition(f, g):
        return lambda x: f(g(x))

    def _op(x, y):
        return max(x, y)

    # st = LazySegTree(op=_op,
    #                  e=_e,
    #                  mapping=lambda f, ixh: (ixh[0], ixh[1], f(ixh[2])),
    #                  composition=_composition,
    #                  id_=lambda x: x,
    #                  v=[(i, x, h) for i, (x, h) in enumerate(XH)])
    st = Lazysegtree(N, 0)
    st.build(H)

    ans = 0
    for i in range(N):
        h = st.get(i)
        if h <= 0:
            continue
        j = bisect.bisect(X, X[i] + 2 * D)
        ac = h // A + (1 if h % A else 0)
        st.add(i, j, -A*ac)
        ans += ac
    print(ans)


class Lazysegtree:  # 区間加算、区間和
    def __init__(self, n, ide_ele):
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        self.depth = self.num.bit_length()

    def build(self, init_val):
        for i, x in enumerate(init_val):
            self.tree[self.num + i] = x
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def gindex(self, l, r):  # 伝播させるブロック（必要なブロックを覆うすべての部分）を求める
        l += self.num
        r += self.num
        lm = (l // (l & (-l))) >> 1  # 下から見た時、伝播する必要のないブロックを求めるもの
        rm = (r // (r & (-r))) >> 1
        res = []
        while l < r:
            if r <= rm: res.append(r)
            if l <= lm: res.append(l)
            l >>= 1
            r >>= 1
        while l:
            res.append(l)
            l >>= 1
        return res

    def propagates(self, idxs):  # lazy配列を伝播
        for i in reversed(idxs):
            v = self.lazy[i]
            if v == 0: continue
            v >>= 1
            self.tree[2 * i] += v
            self.lazy[2 * i] += v
            self.tree[2 * i + 1] += v
            self.lazy[2 * i + 1] += v
            self.lazy[i] = 0

    def add(self, l, r, x):
        """Lazy Segment Treeのapplyとしてxを足す操作を[l, r)の範囲に行う"""
        idxs = self.gindex(l, r)
        l += self.num
        r += self.num
        while l < r:  # 更新ブロックを更新して
            if l & 1:
                self.tree[l] += x
                self.lazy[l] += x
                l += 1
            if r & 1:
                self.tree[r - 1] += x
                self.lazy[r - 1] += x
            l >>= 1
            r >>= 1
            x <<= 1
        for i in idxs:  # 更新ブロックを覆う部分を更新する、更新ブロックより下の部分は更新しない
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1] + self.lazy[i]  # 遅延を考慮

    def get(self, x):
        self.propagates(self.gindex(x, x + 1))
        return self.tree[self.num + x]

    def query(self, l, r):
        self.propagates(self.gindex(l, r))  # 伝播させればあとは普通のセグ木と同じ
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                res += self.tree[r - 1]
            l >>= 1
            r >>= 1
        return res

    def query_all(self):
        return self.tree[1]


def main():
    import sys

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
    solve_2(N, D, A, X, H)
    # solve(N, D, A, X, H)


if __name__ == "__main__":
    main()
