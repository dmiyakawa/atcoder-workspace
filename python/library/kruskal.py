#!/usr/bin/env python
#
# クラスカルのアルゴリズム (Kruskal's Algorithm) を用いた最小全域木 Minimum Spanning Tree の実装
# Union Find Tree が必要
#
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
#

# --本番では差し替え-- #
from union_find_tree import UnionFindTree
# --ここまで-- #


def main():
    import sys
    V, E = [int(e) for e in sys.stdin.readline().split()]
    tree = UnionFindTree()
    for i in range(V):
        tree.make_set(i)

    num_edges = 0
    total_weight = 0
    lst = []
    for i in range(E):
        lst.append(tuple(int(e) for e in sys.stdin.readline().split()))

    for s, t, w in sorted(lst, key=lambda tup: tup[2]):
        if not tree.is_same(s, t):
            tree.unite(s, t)
            num_edges += 1
            total_weight += w
        if num_edges == V - 1:
            break
    assert num_edges == V - 1
    # print(total_weight, end="")
    print(total_weight)


if __name__ == "__main__":
    main()
