#!/usr/bin/env python3


def solve_2(S: str):
    A = ["atcoder".index(ch) for ch in S]
    tree = FenwickTree(7)
    ans = 0
    for i, p in enumerate(A):
        tree.add(p, 1)
        ans += i - tree.sum(0, p)
    print(ans)


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



def solve_1(S: str):
    d = {"atcoder": 0}
    count = 1
    while S not in d:
        keys = list(d.keys())
        for s in keys:
            for i in range(1, len(s)):
                s0 = s[:i - 1] + s[i] + s[i - 1] + s[i + 1:]
                if s0 not in d or d[s0] > count:
                    d[s0] = count
        count += 1
    print(d[S])


def main():
    solve_2(input())


if __name__ == "__main__":
    main()
