#!/usr/bin/env python3
from collections import defaultdict
from typing import List, Dict, Tuple


def solve(N: int, u: int, v: int, A: "List[int]", B: "List[int]"):
    u -= 1
    v -= 1
    E = defaultdict(list)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        E[a].append((1, b))
        E[b].append((1, a))

    d = Dijkstra(N, E)
    distances_u = d.solve(u)
    distances_v = d.solve(v)
    ans = 0
    for du, dv in zip(distances_u, distances_v):
        if du < dv:
            diff = dv - du
            a = du + max(0, diff - 1)
            ans = max(ans, a)
    # print(distances_u)
    # print(distances_v)
    print(ans)


class Dijkstra:
    def __init__(self, N: int, E: "Dict[int, List[Tuple[float, int]]]", inf=float("inf")):
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
                    heapq.heappush(h, (costs[dest], dest))  # type: ignore
        return costs



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = int(next(tokens))  # type: int
    v = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, u, v, A, B)


if __name__ == "__main__":
    main()
