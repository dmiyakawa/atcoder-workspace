class LazySegTree:
    """区間加算 + 区間和"""

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
