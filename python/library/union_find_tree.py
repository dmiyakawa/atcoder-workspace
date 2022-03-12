#!/usr/bin/env python3
#
# Union-Find木
#
# 回答部分は下記問題
# https://atcoder.jp/contests/atc001/tasks/unionfind_a
#
# 関連問題
# https://atcoder.jp/contests/abc229/tasks/abc229_e
#

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = self if parent is None else parent


class UnionFindTree:
    def __init__(self):
        self._all_nodes = {}

    def make_set(self, value):
        assert value not in self._all_nodes
        self._all_nodes[value] = Node(value=value)

    def unite(self, value_1, value_2):
        rank_1 = 1
        node_1 = self._all_nodes[value_1]
        while node_1.parent != node_1:
            rank_1 += 1
            node_1 = node_1.parent

        rank_2 = 1
        node_2 = self._all_nodes[value_2]
        while node_2.parent != node_2:
            rank_2 += 1
            node_2 = node_2.parent
        if node_1.value != node_2.value:
            if rank_1 < rank_2:
                node_1.parent = node_2
            else:
                node_2.parent = node_1

    def is_same(self, value_1, value_2):
        nodes_to_reset_root_1 = set()
        node_1 = self._all_nodes[value_1]
        while node_1.parent != node_1:
            nodes_to_reset_root_1.add(node_1)
            node_1 = node_1.parent
        for n in nodes_to_reset_root_1:
            n.parent = node_1

        nodes_to_reset_root_2 = set()
        node_2 = self._all_nodes[value_2]
        while node_2.parent != node_2:
            nodes_to_reset_root_2.add(node_2)
            node_2 = node_2.parent
        for n in nodes_to_reset_root_2:
            n.parent = node_2

        ret = (node_1.value == node_2.value)

        return ret


def main():
    """\
    https://atcoder.jp/contests/atc001/tasks/unionfind_a
    """
    import sys
    N, Q = [int(e) for e in sys.stdin.readline().split()]
    tree = UnionFindTree()
    for i in range(N):
        tree.make_set(i)

    for i in range(Q):
        p, a, b = [int(e) for e in sys.stdin.readline().split()]
        if p == 0:
            tree.unite(a, b)
        else:
            assert p == 1
            print("Yes" if tree.is_same(a, b) else "No")


if __name__ == "__main__":
    main()
