#!/usr/bin/env python3


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = self if parent is None else parent


class UnionFindTree:
    def __init__(self):
        self._all_nodes = {}

    @property
    def all_nodes(self):
        return self._all_nodes

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
        if value_1 not in self._all_nodes or value_2 not in self._all_nodes:
            return False
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
    H, W = [int(e) for e in input().split()]
    Q = int(input())

    uf_tree = UnionFindTree()

    for _ in range(Q):
        lst = [int(e) for e in input().split()]
        if lst[0] == 1:
            h, w = lst[1:]
            node = (h, w)
            uf_tree.make_set((h, w))
            for adj in [(h - 1, w), (h, w - 1), (h + 1, w), (h, w + 1)]:
                if adj in uf_tree.all_nodes:
                    uf_tree.unite(node, adj)
        else:
            h1, w1, h2, w2 = lst[1:]
            print("Yes" if uf_tree.is_same((h1, w1), (h2, w2)) else "No")


if __name__ == "__main__":
    main()
