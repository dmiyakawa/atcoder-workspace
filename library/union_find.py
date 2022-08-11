#!/usr/bin/env python3
"""\
UnionFind木。ベースは https://atcoder.jp/contests/abc206/submissions/30722903
"""


class UnionFind:
    def __init__(self, n: int):
        """[0, N-1]をノードとするUnionFind木を作成する"""
        self._n = n
        # 正のとき、親を表す。負のとき、そのインデックスはグループのrootで、その数値の絶対値はグループのサイズを表す
        self._parents = [-1] * n

    def find(self, x: int) -> int:
        """グループの根を見つける。自分が根であるときは自分自身の値を返す"""
        if self._parents[x] < 0:
            return x
        else:
            # 経路圧縮している
            self._parents[x] = self.find(self._parents[x])
            return self._parents[x]

    def unite(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self._parents[x] > self._parents[y]:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x

    def size(self, x) -> int:
        return -self._parents[self.find(x)]

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x) -> "List[int]":
        """O(N)"""
        root = self.find(x)
        return [i for i in range(self._n) if self.find(i) == root]

    def roots(self) -> "List[int]":
        return [i for i, x in enumerate(self._parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self):
        ret = {}
        for i in range(self._n):
            ret.setdefault(self.find(i), []).append(i)
        return ret

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


def main():
    """https://atcoder.jp/contests/atc001/tasks/unionfind_a"""
    N, Q = [int(e) for e in input().split()]
    tree = UnionFind(N)
    for i in range(Q):
        p, a, b = [int(e) for e in input().split()]
        if p == 0:
            tree.unite(a, b)
        else:
            assert p == 1
            print("Yes" if tree.same(a, b) else "No")


if __name__ == "__main__":
    main()
