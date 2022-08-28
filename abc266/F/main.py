#!/usr/bin/env python3
from collections import defaultdict

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, U: "List[int]", V: "List[int]", Q: int, X: "List[int]", Y: "List[int]"):
    links = defaultdict(set)
    for u, v in zip(U, V):
        u -= 1
        v -= 1
        links[u].add(v)
        links[v].add(u)

    uf = UnionFind(N)
    loop = None

    visited = set()
    stack = []

    def dfs_loop(_u, _prev):
        nonlocal loop

        if _u in visited:
            return False
        visited.add(_u)
        stack.append((_u, _prev))
        if _prev is not None:
            uf.unite(_prev, _u)
        for _v in links[_u]:
            if _v == _prev:
                continue
            if uf.same(_u, _v):
                loop = {_v, _u}
                stack.pop()
                while stack:
                    _n, _p = stack.pop()
                    if _n == _v:
                        break
                    if _n != _prev:
                        continue
                    loop.add(_n)
                    _prev = _p
                return True
            else:
                ret = dfs_loop(_v, _u)
                if ret:
                    return True

    dfs_loop(0, None)
    # print(loop)

    uf = UnionFind(N)
    for n, l in links.items():
        if len(l) == 1:
            to_visit = [n]
            visited = set()
            while to_visit:
                u = to_visit.pop()
                if u in visited:
                    continue
                visited.add(u)
                for v in links[u]:
                    if v in visited or (u in loop and v in loop) or uf.same(u, v):
                        continue
                    uf.unite(u, v)
                    to_visit.append(v)
    # print(uf)
    for x, y in zip(X, Y):
        if uf.same(x - 1, y - 1):
            print("Yes")
        else:
            print("No")



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
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, u, v, Q, x, y)


if __name__ == "__main__":
    main()
