#!/usr/bin/env python3


def solve_ref(N, Q, L, R):
    """https://atcoder.jp/contests/abc238/editorial/3360"""
    uf = UnionFind(N + 1)
    for l, r in zip(L, R):
        l -= 1
        uf.unite(l, r)
    print("Yes" if uf.same(0, N) else "No")


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


def solve_ref2(N, Q, L, R):
    from collections import defaultdict
    links = defaultdict(set)
    for l, r in zip(L, R):
        links[l - 1].add(r)
        links[r].add(l - 1)

    to_visit = [0]
    visited = set()
    while to_visit:
        n = to_visit.pop()
        if n in visited:
            continue
        visited.add(n)
        for m in links[n]:
            if m == N:
                print("Yes")
                return
            if m in visited:
                continue
            to_visit.append(m)
    print("No")


def main():
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    L, R = [0] * Q, [0] * Q
    for i in range(Q):
        L[i], R[i] = map(int, input().split())
    solve_ref2(N, Q, L, R)


if __name__ == "__main__":
    main()
