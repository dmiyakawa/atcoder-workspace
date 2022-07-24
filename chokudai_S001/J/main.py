#!/usr/bin/env python3

def solve(N, A) -> int:
    tree = FenwickTree(N + 1)
    ans = 0
    for i, p in enumerate(A):
        tree.add(p, 1)
        ans += i - tree.sum(0, p)
    return ans


class FenwickTree:
    """\
    長さ N の配列に対し、

    - 要素の 1 点変更
    - 区間の要素の総和

    を O(logN) で求めることが出来るデータ構造

    Reference: https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int):
        """[left, right) の和を求める"""
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(solve(N, A))


if __name__ == "__main__":
    main()
