#!/usr/bin/env python3


def solve_ref(N: int, M: int, X: "List[int]", Y: "List[int]", A: "List[int]", B: "List[int]", Z: "List[int]"):
    """解説読後"""
    costs = [(a - 1, b - 1, z) for a, b, z in zip(A, B, Z)]

    # 空港をindex N, 港をindex N + 1
    for i, (x, y) in enumerate(zip(X, Y)):
        costs.append((i, N, x))
        costs.append((i, N + 1, y))
    costs.sort(key=lambda tup: tup[2])

    # クラスカルのアルゴリズムを空港・港の有無を考慮して4パターンに対して行う
    min_cost = float("inf")
    for i in range(4):
        uf = UnionFind(N + 2)
        total = 0
        for j, (u, v, cost) in enumerate(costs):
            if i == 0 and (u >= N or v >= N):
                continue
            elif i == 1 and (u == N + 1 or v == N + 1):
                continue
            elif i == 2 and (u == N or v == N):
                continue
            if uf.same(u, v):
                continue
            uf.unite(u, v)
            total += cost
        if uf.size() != (1 if i == 3 else (2 if i > 0 else 3)):
            continue
        min_cost = min(min_cost, total)
    print(min_cost)


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
    M = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Y = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    Z = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve_ref(N, M, X, Y, A, B, Z)


if __name__ == "__main__":
    main()
