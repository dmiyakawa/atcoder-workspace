#!/usr/bin/env python3
#
# 無向グラフ型ダイクストラ
#
# https://atcoder.jp/contests/typical90/tasks/typical90_m
#

from typing import List, Dict, Tuple


class Dijkstra:
    def __init__(self, N: int, E: Dict[int, List[Tuple[int, int]]], inf=1 << 60):
        self.N = N
        self.E = E
        self.inf = inf

    def solve(self, start: int) -> List[int]:
        """sから他のノードの最短距離をリストで返す"""
        import heapq

        costs = [self.inf] * self.N
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
                    heapq.heappush(h, (costs[dest], dest))
        return costs


class DijkstraP:
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
