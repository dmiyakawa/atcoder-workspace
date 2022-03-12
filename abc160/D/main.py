#!/usr/bin/env python3
#
# ref.
# https://twitter.com/e869120/status/1382101716066127872/photo/1
#

import heapq
import math
from typing import List, Dict, Any


Score = int


class DijkstraNode:
    def __init__(self, node_id: int, cost: Score, prev: Any):
        self.node_id = node_id
        self.cost = cost
        self.prev = prev

    def __lt__(self, other: "DijkstraNode"):
        return self.cost < other.cost

    def __hash__(self):
        return hash(self.node_id)

    def __str__(self):
        return "<{}, {}, {}>".format(self.node_id, self.cost, self.prev.node_id if self.prev else None)

    __repr__ = __str__


def do_dijkstra(N: int, links: Dict[int, Dict[int, Score]], start_id: int) -> List[DijkstraNode]:
    nodes: List[DijkstraNode] = [DijkstraNode(i, 0 if i == start_id else math.inf, None) for i in range(N + 1)]
    remaining: List[DijkstraNode] = [nodes[start_id]]
    while remaining:
        cur_node = heapq.heappop(remaining)

        for next_node_id, cost in links.get(cur_node.node_id, {}).items():
            next_node = nodes[next_node_id]
            if next_node.cost > cur_node.cost + cost:
                next_node.cost = cur_node.cost + cost
                next_node.prev = cur_node
                heapq.heappush(remaining, next_node)

    return nodes


def solve(N: int, X: int, Y: int):
    links: Dict[int, Dict[int, Score]] = {}
    for i in range(1, N):
        links.setdefault(i, {})[i + 1] = 1
        links.setdefault(i + 1, {})[i] = 1
    links[X][Y] = 1
    links[Y][X] = 1

    nodes_lst: List[List[DijkstraNode]] = []
    for i in range(1, N + 1):
        nodes_lst.append(do_dijkstra(N, links, start_id=i))
    d = {}
    for nodes in nodes_lst:
        for node in nodes:
            d[node.cost] = d.get(node.cost, 0) + 1
    for k in range(1, N):
        print(d.get(k, 0) // 2)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, X, Y)


if __name__ == "__main__":
    main()
