class SegTree:
    def __init__(self, init_val, op, ide_ele):
        n = len(init_val)
        self._op = op
        self._e = ide_ele
        self._num = 1 << (n - 1).bit_length()
        self._tree = [ide_ele] * 2 * self._num
        for i in range(n):
            self._tree[self._num + i] = init_val[i]
        for i in range(self._num - 1, 0, -1):
            self._tree[i] = self._op(self._tree[2 * i], self._tree[2 * i + 1])

    def set(self, k, x):
        k += self._num
        self._tree[k] = x
        while k > 1:
            self._tree[k >> 1] = self._op(self._tree[k], self._tree[k ^ 1])
            k >>= 1

    def prod(self, l, r):
        res = self._e

        l += self._num
        r += self._num
        while l < r:
            if l & 1:
                res = self._op(res, self._tree[l])
                l += 1
            if r & 1:
                res = self._op(res, self._tree[r - 1])
            l >>= 1
            r >>= 1
        return res
