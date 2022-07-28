#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict, List, Tuple, Any


def main():
    E = defaultdict(list)
    links: Dict[Tuple[int, int], int] = {}
    N, M = map(int, input().split())
    for i in range(M):
        a, b, c = [int(e) - 1 for e in input().split()]
        E[a].append((c, b))
        E[b].append((c, a))
        links[(a, b)] = i
    di = DijkstraP(N, E)
    costs, prevs = di.solve(0)
    ans = []
    for i, j in enumerate(prevs[1:], start=1):
        tup: Any = tuple(sorted([i, j]))
        ans.append(links[tup])
    print(*ans)


class DijkstraP:
    """バックトラック用のノード番号が返されるバージョン"""
    def __init__(self, N: int, E: Dict[int, List[Tuple[int, int]]], inf=1 << 60):
        self.N = N
        self.E = E
        self.inf = inf

    def solve(self, start: int) -> Tuple[List[int], List[int]]:
        import heapq

        costs = [self.inf] * self.N
        prevs = [-1] * self.N
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
                    prevs[dest] = v
                    heapq.heappush(h, (costs[dest], dest))
        return costs, prevs

if __name__ == "__main__":
    main()
