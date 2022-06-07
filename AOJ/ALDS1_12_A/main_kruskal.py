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

    def is_same(self, value_1, value_2) -> bool:
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


def solve_with_kruskal(N, grid):
    tree = UnionFindTree()
    lst = []
    for i in range(N):
        tree.make_set(i)
        for j in range(i + 1, N):
            if grid[i][j] < 0:
                continue
            lst.append((i, j, grid[i][j]))
            lst.append((j, i, grid[i][j]))

    total_weight = 0
    num_edges = 0
    for s, t, w in sorted(lst, key=lambda tup: tup[2]):
        if not tree.is_same(s, t):
            tree.unite(s, t)
            num_edges += 1
            total_weight += w
        if num_edges == N - 1:
            break
    print(total_weight)


def main():
    N = int(input())
    grid = [[int(e) for e in input().split()] for _ in range(N)]
    solve_with_kruskal(N, grid)


if __name__ == "__main__":
    main()
