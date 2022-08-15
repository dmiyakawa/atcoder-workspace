#!/usr/bin/env python3

import heapq
import sys
from typing import Dict, List, Tuple, Set

input = sys.stdin.readline
Inf = INF = float("INF")


def main():
    H, W = map(int, input().split())
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A = [[int(e) for e in input().split()] for _ in range(H)]
    # dp[h][w][fr][fc]
    # fr ... その行をフリップしたら1
    # fc ... その列をフリップしたら1
    dp = [Inf] * H * W * 4

    def _addr(h, w, fr, fc) -> int:
        return h * W * 4 + w * 4 + fr * 2 + fc

    dp[_addr(0, 0, 0, 0)] = 0
    dp[_addr(0, 0, 1, 0)] = R[0]
    dp[_addr(0, 0, 0, 1)] = C[0]
    dp[_addr(0, 0, 1, 1)] = C[0] + R[0]
    h = [(0, (0, 0), set(), set()),
         (R[0], (0, 0), {0}, set()),
         (C[0], (0, 0), set(), {0}),
         (R[0] + C[0], (0, 0), {0}, {0})]
    heapq.heapify(h)
    visited: Set[Tuple[int, int]] = set()
    while len(h) > 0:
        cost, node, rows, cols = heapq.heappop(h)
        if node in visited:
            continue
        visited.add(node)
        h, w = node
        a_c = (A[h][w] + (1 if h in rows else 0) + (1 if w in cols else 0)) % 2
        for h0, w0 in [(h - 1, w), (h, w - 1), (h + 1, w), (h, w + 1)]:
            if (h0, w0) in visited:
                continue
            if A[h0][w0] == a_c:
                ...




class Dijkstra:
    def __init__(self, N: int, E: Dict[int, List[Tuple[float, int]]], inf=float("inf")):
        self.N = N
        # (cost, dest) のリスト
        self.E = E
        self.inf = inf

    def solve(self, start: int) -> "List[int]":
        """sから他のノードの最短距離をリストで返す"""


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




if __name__ == "__main__":
    main()
