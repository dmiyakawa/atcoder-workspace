#!/usr/bin/env python3
#
# 無向グラフ型ダイクストラ
#
# https://atcoder.jp/contests/typical90/tasks/typical90_m
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


def main():
    import sys

    N, M = [int(e) for e in sys.stdin.readline().split()]
    links: Dict[int, Dict[int, int]] = {}
    for i in range(M):
        a, b, c = [int(e) for e in sys.stdin.readline().split()]
        links.setdefault(a, {})[b] = c
        links.setdefault(b, {})[a] = c

    nodes_1 = do_dijkstra(N, links, start_id=1)
    nodes_n = do_dijkstra(N, links, start_id=N)
    for i in range(1, N + 1):
        print(nodes_1[i].cost + nodes_n[i].cost)


if __name__ == "__main__":
    main()
