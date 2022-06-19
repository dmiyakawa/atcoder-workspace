#!/usr/bin/env python3


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self._segfunc = segfunc
        self._e = ide_ele
        self._num = 1 << (n - 1).bit_length()
        self._tree = [ide_ele] * 2 * self._num
        for i in range(n):
            self._tree[self._num + i] = init_val[i]
        for i in range(self._num - 1, 0, -1):
            self._tree[i] = self._segfunc(self._tree[2 * i], self._tree[2 * i + 1])

    def set(self, k, x):
        k += self._num
        self._tree[k] = x
        while k > 1:
            self._tree[k >> 1] = self._segfunc(self._tree[k], self._tree[k ^ 1])
            k >>= 1

    def prod(self, l, r):
        res = self._e

        l += self._num
        r += self._num
        while l < r:
            if l & 1:
                res = self._segfunc(res, self._tree[l])
                l += 1
            if r & 1:
                res = self._segfunc(res, self._tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def mod_inverse(x, p):
    """xの逆数 (mod p) を返す"""
    # フェルマーの小定理からxの逆数をx'とすると x' = x^(p-2) mod p
    k = p - 2
    ret = 1
    y = x
    while k:
        if k & 1:
            ret = (ret * y) % p
        y = (y * y) % p
        k //= 2
    return ret


MOD = 998244353  # type: int


def main_ans():
    # https://atcoder.jp/contests/abc256/submissions/32578670

    def segfunc(_x, _y):
        return (_x + _y) % MOD

    N, Q = map(int, input().split())
    a = [0]
    a1 = [0]
    a2 = [0]

    for i, val in enumerate(map(int, input().split()), start=1):
        a.append(val % MOD)
        a1.append(i * val % MOD)
        a2.append(i * i * val % MOD)

    seg = SegTree(a, segfunc, 0)
    seg1 = SegTree(a1, segfunc, 0)
    seg2 = SegTree(a2, segfunc, 0)
    inv = mod_inverse(2, MOD)

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            _, x, v = query
            seg.set(x, v % MOD)
            seg1.set(x, x * v % MOD)
            seg2.set(x, x * x * v % MOD)
        else:
            _, x = query
            ans = (((seg.prod(0, x + 1) % MOD) * (x + 1) % MOD) * (x + 2) * inv) % MOD
            ans = ans + (-seg1.prod(0, x + 1) * (2 * x + 3) + seg2.prod(0, x + 1)) * inv
            print(ans % MOD)


if __name__ == "__main__":
    main_ans()
