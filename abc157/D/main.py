#!/usr/bin/env python3

import sys
from collections import defaultdict


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    uf = UnionFind(N)

    links = defaultdict(set)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        uf.unite(a, b)
        links[a].add(b)
        links[b].add(a)

    blocked = defaultdict(set)
    for c, d in zip(C, D):
        c -= 1
        d -= 1
        if uf.same(c, d):
            blocked[c].add(d)
            blocked[d].add(c)

    ans = [-1] * N
    for members in uf.all_group_members().values():
        for i in members:
            ans[i] = len(members) - len(links[i]) - len(blocked[i]) - 1

    print(*ans)


class UnionFind:
    def __init__(self, n: int):
        """[0, N-1]をノードとするUnionFind木を作成する"""
        self._n = n
        # 正のとき、親を表す。負のとき、そのインデックスはグループのrootで、その数値の絶対値はグループのサイズを表す
        self._parents = [-1] * n
        # experimental
        self._roots = {i for i in range(n)}

    def find(self, x: int) -> int:
        """グループの根を見つける。自分が根であるときは自分自身の値を返す"""
        if self._parents[x] < 0:
            return x
        # 経路圧縮している
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def unite(self, x: int, y: int) -> int:
        """要素のグループが異なるようならそれらのグループを統合して、共通のrootを返す"""
        x, y = self.find(x), self.find(y)
        if x == y:
            return x

        if self._parents[x] > self._parents[y]:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x
        self._roots.remove(y)
        return x

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x) -> "List[int]":
        """xが属するグループの要素をリストで返す。O(N)"""
        root = self.find(x)
        return [i for i in range(self._n) if self.find(i) == root]

    def roots(self) -> "List[int]":
        """rootとなる要素を返す。O(N)"""
        return [i for i, x in enumerate(self._parents) if x < 0]

    def roots2(self) -> "Collection[int]":
        # freezeしてないので危険かも
        return self._roots

    def group_size(self, x) -> int:
        """xが属するグループのサイズを返す"""
        return -self._parents[self.find(x)]

    def size(self) -> int:
        # experimental
        return len(self._roots)

    def group_count(self) -> int:
        """グループ数を返す。O(N)"""
        return len(self.roots())

    def all_group_members(self):
        """O(N)"""
        ret = {}
        for i in range(self._n):
            ret.setdefault(self.find(i), []).append(i)
        return ret

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, K, A, B, C, D)


if __name__ == "__main__":
    main()
