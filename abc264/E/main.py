#!/usr/bin/env python3

# スピードが段違い……
# - あり (735 ms)  https://atcoder.jp/contests/abc264/submissions/34035700
# - なし (1252 ms) https://atcoder.jp/contests/abc264/submissions/34035721
import sys
input = sys.stdin.readline


def solve(N, U, V, X):
    """初AC は https://atcoder.jp/contests/abc264/submissions/34035139"""
    Xs = set(X)
    all_links = []
    uf = UnionFind(N + 1)
    for i, (u, v) in enumerate(zip(U, V)):
        if N < u:
            u = 0
        if N < v:
            v = 0
        all_links.append((u, v))
        if i in Xs:
            continue
        uf.unite(u, v)

    towns = {root: len([i for i in members if 1 <= i <= N]) for root, members in uf.all_group_members().items()}

    rev_ans = []
    for x in X[::-1]:
        rev_ans.append(towns.get(uf.find(0), 0))
        u, v = all_links[x]
        root_u, root_v = uf.find(u), uf.find(v)
        if root_u == root_v:
            continue
        new_towns = towns[root_u] + towns[root_v]
        del towns[root_v]
        del towns[root_u]
        towns[uf.unite(root_u, root_v)] = new_towns

    for ans in rev_ans[::-1]:
        print(ans)


def main():
    N, M, E = list(map(int, input().split()))
    U, V = [0] * E, [0] * E
    for i in range(E):
        u, v = map(int, input().split())
        U[i] = 0 if N < u else u
        V[i] = 0 if N < v else v
    Q = int(input())
    X = [int(input()) - 1 for _ in range(Q)]
    solve(N, U, V, X)


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
            return x

        if self._parents[x] > self._parents[y]:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x
        return x

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


if __name__ == "__main__":
    main()
