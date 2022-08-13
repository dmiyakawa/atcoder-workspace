#!/usr/bin/env python3

import sys
from collections import defaultdict


def solve(N: int, M: int, E: int, U: "List[int]", V: "List[int]", Q: int, X: "List[int]"):
    all_links = []
    Xs = set(X)

    # 都市 [0, N-1], 発電所 [N, N + M - 1]
    uf = UnionFind(N + M)

    connected_roots = {n for n in range(N, N + M)}
    for i, (u, v) in enumerate(zip(U, V)):
        u -= 1
        v -= 1
        all_links.append((u, v))
        if i + 1 in Xs:
            continue

        uf.unite(u, v)

        if N <= u < N + M - 1 or N <= v < N + M - 1:
            connected_roots.add(uf.find(u))

    root_to_towns = defaultdict(set)
    connected_towns = set()
    for root, members in uf.all_group_members().items():
        for i in members:
            if i < N:
                root_to_towns[root].add(i)
                if root in connected_roots:
                    connected_towns.add(i)


    rev_ans = [len(connected_towns)]
    for i, x in enumerate(reversed(X)):
        x -= 1
        u, v = all_links[x]
        root_u = uf.find(u)
        root_v = uf.find(v)

        # print(f"i: {i}, u: {u} ({root_u}), v: {v} ({root_v}), connected_towns: {connected_towns}, connected_roows: {connected_roots}")

        if root_u == root_v:
            pass
        elif root_u in connected_roots and root_v in connected_roots:
            uf.unite(u, v)
        elif root_u in connected_roots and root_v not in connected_roots:
            for town in root_to_towns[root_v]:
                connected_towns.add(town)
            uf.unite(u, v)
            connected_roots.add(root_u)
        elif root_u not in connected_roots and root_v in connected_roots:
            for town in root_to_towns[root_u]:
                connected_towns.add(town)
            uf.unite(u, v)
            connected_roots.add(root_v)
        else:
            assert root_u not in connected_roots
            assert root_v not in connected_roots
            root = uf.unite(u, v)
            new_towns = root_to_towns[u] | root_to_towns[v]
            root_to_towns[root] = new_towns

        rev_ans.append(len(connected_towns))
    for ans in list(reversed(rev_ans))[1:]:
        print(ans)


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

        # 改変
        if self._parents[x] < self._parents[y]:
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




def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    U = [int()] * (E)  # type: "List[int]"
    V = [int()] * (E)  # type: "List[int]"
    for i in range(E):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, M, E, U, V, Q, X)


if __name__ == "__main__":
    main()
