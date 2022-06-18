#!/usr/bin/env python3
from collections import defaultdict
from typing import Dict, Set

MOD = 998244353  # type: int


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


def main():
    N, M = map(int, input().split())
    print(solve(N, M))


def solve(N, M):
    uf = UnionFind(N)
    links = defaultdict(set)
    for _ in range(M):
        u, v = [int(e) - 1 for e in input().split()]
        links[u].add(v)
        uf.unite(u, v)

    groups = uf.all_group_members()

    for group in groups.values():
        num_nodes = len(group)
        num_links = 0
        for n in group:
            num_links += len(links[n])

        if num_links != num_nodes:
            return 0
    return 2 ** len(groups) % MOD


if __name__ == "__main__":
    main()
