#!/usr/bin/env python3

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


def do_dijkstra(floors: List[int], links: Dict[int, Dict[int, Score]], start_id: int) -> Dict[int, DijkstraNode]:
    nodes: Dict[int, DijkstraNode] = {i: DijkstraNode(i, 0 if i == start_id else math.inf, None) for i in floors}
    remaining: List[DijkstraNode] = [nodes[start_id]]
    visited = set()
    while remaining:
        cur_node = heapq.heappop(remaining)
        if cur_node.node_id in visited:
            continue
        visited.add(cur_node.node_id)

        for next_node_id, cost in links.get(cur_node.node_id, {}).items():
            next_node = nodes[next_node_id]
            if next_node.cost > cur_node.cost + cost:
                next_node.cost = cur_node.cost + cost
                next_node.prev = cur_node
                heapq.heappush(remaining, next_node)

    return nodes


def main():
    N, M = [int(e) for e in input().split()]
    floors_set = {1, N}
    links: Dict[int, Dict[int, int]] = {}
    for _ in range(M):
        a, b, c = [int(e) for e in input().split()]
        d1 = links.setdefault(a, {})
        d1[b] = min(d1.get(b, math.inf), c)
        d2 = links.setdefault(b, {})
        d2[a] = min(d2.get(a, math.inf), c)

        floors_set.add(a)
        floors_set.add(b)

    floors = sorted(floors_set)

    for i in range(1, len(floors)):
        prev_fl = floors[i - 1]
        cur_fl = floors[i]
        cost = abs(cur_fl - prev_fl)
        d1 = links.setdefault(cur_fl, {})
        d1[prev_fl] = min(d1.get(prev_fl, math.inf), cost)
        d2 = links.setdefault(prev_fl, {})
        d2[cur_fl] = min(d2.get(cur_fl, math.inf), cost)

    nodes = do_dijkstra(floors, links, 1)

    print(nodes[N].cost)


if __name__ == "__main__":
    main()
