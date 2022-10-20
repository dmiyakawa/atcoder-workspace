#!/usr/bin/env python3

from collections import defaultdict
from typing import Collection, List, Tuple


def solve(H: int, W: int, line: "List[str]"):
    N = H*W
    E = defaultdict(set)
    si = -1
    gi = -1
    bis = set()
    for h, l in enumerate(line):
        for w, ch in enumerate(l):
            i = h * W + w
            if ch == "#":
                bis.add(i)
                continue
            if ch == "S":
                si = i
            if ch == "G":
                gi = i
            for h0, w0 in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                h1, w1 = h + h0, w + w0
                if not (0 <= h1 < H and 0 <= w1 < W):
                    continue
                j = h1*W + w1
                E[i].add((1, j))
    assert si >= 0
    assert gi >= 0

    dijkstra = Dijkstra(N, E)
    costs_from_start = dijkstra.solve(si)
    costs_from_goal = dijkstra.solve(gi)
    assert costs_from_start[gi] > N
    assert costs_from_goal[si] > N
    max_cost = 0
    for bi in bis:
        c1 = costs_from_start[bi]
        c2 = costs_from_goal[bi]
        if c1 > N or c2 > N:
            continue
        max_cost = max(max_cost, c1 + c2)
    print(max_cost)


class Dijkstra:
    def __init__(self, N: int, E: "Dict[int, Collection[Tuple[float, int]]]", inf=float("inf")):
        self.N = N
        # (cost, dest) のリスト。heapqに突っ込むことを想定してcostがタプルの先頭になっていることに注意
        self.E = E
        self.inf = inf

    def solve(self, start: int) -> "List[int]":
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


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    line = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, line)


if __name__ == "__main__":
    main()
