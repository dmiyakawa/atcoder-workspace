#!/usr/bin/env python3

"""\
長さ N の配列に対し、
- 要素の 1 点変更
- 区間の要素の総和
を O(logN) で求めることが出来るデータ構造。BIT (Binary Indexed Tree)とも呼ばれる
Reference: https://en.wikipedia.org/wiki/Fenwick_tree
"""

class FenwickTree:
    def __init__(self, n: int = 0) -> None:
        """nはデータサイズ"""
        self._n = n
        self._data = [0] * n

    def add(self, p: int, x) -> None:
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self._data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> int:
        """[left, right) の和を求める"""
        assert 0 <= left <= right <= self._n
        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> int:
        s = 0
        while r > 0:
            s += self._data[r - 1]
            r -= r & -r
        return s


def _main():
    # https://atcoder.jp/contests/practice2/tasks/practice2_b
    N, Q = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    tree = FenwickTree(N)
    for i, a in enumerate(A):
        tree.add(i, a)

    for _ in range(Q):
        query = [int(e) for e in input().split()]
        op = query[0]
        if op == 0:
            p, x = query[1:]
            tree.add(p, x)
        else:
            l, r = query[1:]
            print(tree.sum(l, r))


if __name__ == "__main__":
    _main()
