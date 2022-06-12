#!/usr/bin/env python3
from collections import defaultdict
from typing import List, Dict, Tuple


class Dijkstra:
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


def main():
    from functools import reduce
    N, M = map(int, input().split())
    E = defaultdict(list)
    for _ in range(M):
        a, b = [int(e) - 1 for e in input().split()]
        E[a].append((1, b))
        E[b].append((1, a))
    solver = Dijkstra(N, E)
    costs, prevs = solver.solve(0)
    if not reduce(lambda x, y: x and y != -1, prevs[1:], True):
        print("No")
        return
    print("Yes")
    for prev in prevs[1:]:
        print(prev + 1)


if __name__ == "__main__":
    main()
