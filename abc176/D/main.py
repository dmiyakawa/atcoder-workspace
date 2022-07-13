#!/usr/bin/env python3

from collections import defaultdict, deque
from typing import Dict, List, Tuple, Iterable, Set


Inf = 1 << 60


def solve2_tle(H, W, Ch, Cw, Dh, Dw, S):
    # 解説の 01-BFS を使用して実装. TLE
    # https://atcoder.jp/contests/abc176/editorial/65

    def _is_visitable(_h, _w):
        return 0 <= _h < H and 0 <= _w < W and S[_h][_w] == "."

    dq = deque()
    dq.append((Ch, Cw))
    min_costs = {(Ch, Cw): 0}

    while dq:
        h, w = dq.popleft()
        cost = min_costs[(h, w)]
        if (h, w) == (Dh, Dw):
            return cost
        adjs = [(h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)]
        for (h1, w1) in adjs:
            if not _is_visitable(h1, w1):
                continue
            if min_costs.get((h1, w1), Inf) <= cost:
                continue
            min_costs[(h1, w1)] = cost
            dq.appendleft((h1, w1))
        for h1 in range(max(0, h - 2), min(h + 3, H)):
            for w1 in range(max(0, w - 2), min(w + 3, W)):
                if (h, w) == (h1, w1) or (h1, w1) in adjs or not _is_visitable(h1, w1):
                    continue
                if min_costs.get((h1, w1), Inf) <= cost + 1:
                    continue
                min_costs[(h1, w1)] = cost + 1
                dq.append((h1, w1))
    return -1


def solve(H, W, Ch, Cw, Dh, Dw, S):
    # 初AC時
    # Union-Find + Dijkstra

    def get_id(h, w):
        return W * h + w

    uf = UnionFind(H * W)

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            _id = get_id(i, j)
            if i > 0 and S[i - 1][j] == ".":
                uf.unite(_id, get_id(i - 1, j))

            if j > 0 and S[i][j - 1] == ".":
                uf.unite(_id, get_id(i, j - 1))

    start = uf.find(get_id(Ch, Cw))
    dest = uf.find(get_id(Dh, Dw))
    links: Dict[int, Set[Tuple[int, int]]] = defaultdict(set)
    # print(start, dest, uf.all_group_members())

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            _id1 = get_id(i, j)
            # print(i, j, _id1, uf.find(_id1))
            for i2 in range(max(0, i - 2), min(i + 3, H)):
                for j2 in range(max(0, j - 2), min(j + 3, W)):
                    if S[i2][j2] == "#":
                        continue
                    _id2 = get_id(i2, j2)
                    # print(" ", i, j, _id2, uf.find(_id2))
                    p1 = uf.find(_id1)
                    p2 = uf.find(_id2)
                    if p1 != p2:
                        links[p1].add((1, p2))
                        links[p2].add((1, p1))

    di = Dijkstra(N=H*W, E=links)
    result = di.solve(start)
    ans = result[dest]
    print(-1 if ans == Inf else ans)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        ret = {}
        for i in range(self.n):
            ret.setdefault(self.find(i), []).append(i)
        return ret

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


class Dijkstra:
    def __init__(self, N: int, E: Dict[int, Iterable[Tuple[int, int]]], inf=Inf):
        self.N = N
        # (cost, dest) のリスト
        self.E = E
        self.inf = inf

    def solve(self, start: int) -> List[int]:
        """sから他のノードの最短距離をリストで返す"""
        import heapq

        costs = [self.inf] * self.N
        costs[start] = 0
        h = [(0, start)]
        visited = set()

        while len(h) > 0:
            _, v = heapq.heappop(h)
            if v in visited:
                continue
            visited.add(v)

            for cost, dest in self.E[v]:
                if costs[dest] > costs[v] + cost:
                    costs[dest] = costs[v] + cost
                    heapq.heappush(h, (costs[dest], dest))
        return costs


def main():
    H, W = map(int, input().split())
    Ch, Cw = [int(e) - 1 for e in input().split()]
    Dh, Dw = [int(e) - 1 for e in input().split()]
    S = [input() for _ in range(H)]
    print(solve2_tle(H, W, Ch, Cw, Dh, Dw, S))


if __name__ == "__main__":
    main()
