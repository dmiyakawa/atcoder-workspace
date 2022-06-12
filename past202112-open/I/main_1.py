#!/usr/bin/env python3

import heapq
import math
from typing import List, Dict, Tuple


def do_dijkstra(floors: List[int], links: Dict[int, Dict[int, int]], start_id: int) -> Dict[int, float]:
    costs: Dict[int, float] = {i: 0 if i == start_id else math.inf for i in floors}
    remaining: List[Tuple[float, int]] = [(0, start_id)]
    visited = set()

    while remaining:
        cur_node = heapq.heappop(remaining)
        if cur_node[1] in visited:
            continue
        visited.add(cur_node[1])

        for next_node_id, cost in links.get(cur_node[1], {}).items():
            current_cost = costs[next_node_id]
            if current_cost > cur_node[0] + cost:
                costs[next_node_id] = cur_node[0] + cost
                heapq.heappush(remaining, (cur_node[0] + cost, next_node_id))

    return costs


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

    print(nodes[N])


if __name__ == "__main__":
    main()
