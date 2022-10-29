#!/usr/bin/env python3
import math
import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = 1 << 60

def solve(N: int, M: int, x: "List[int]", y: "List[int]",
          c: "List[int]", X: "List[int]", Y: "List[int]", C: "List[int]"):
    ans = Inf
    for mb in range(1<<M):
        X1, Y1, C1 = x.copy(), y.copy(), c.copy()
        for i in range(M):
            if mb >> i & 1:
                X1.append(X[i])
                Y1.append(Y[i])
                C1.append(C[i])
        N1 = len(X1)
        links = []
        for s in range(N1):
            for t in range(N1):
                if s == t:
                    continue
                dist = math.sqrt((X1[s] - X1[t])**2 + (Y1[s] - Y1[t])**2) * (1 if C1[s] == C1[t] else 10)
                links.append((dist, s, t))
        links.sort(reverse=True)
        uf = UnionFind(N1)
        cost = 0
        while uf.size() > 1:
            dist, s, t = links.pop()
            if uf.same(s, t):
                continue
            uf.unite(s, t)
            cost += dist
        ans = min(ans, cost)
    print(ans)


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
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        c[i] = int(next(tokens))
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, x, y, c, X, Y, C)





if __name__ == "__main__":
    main()
