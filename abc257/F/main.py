#!/usr/bin/env python3

import sys
from collections import defaultdict

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, U: "List[int]", V: "List[int]"):
    """AC。コスト1だけなのでダイクストラは過剰"""
    E = defaultdict(list)
    for u, v in zip(U, V):
        E[v].append((1, u))
        if u != 0:
            E[u].append((1, v))

    dj = Dijkstra(N + 1, E, inf=Inf)
    costs_from_1 = dj.solve(1)
    costs_from_N = dj.solve(N)
    lst = []
    for n in range(1, N + 1):
        ans = min(costs_from_1[N], min(costs_from_1[0], costs_from_1[n]) + min(costs_from_N[0], costs_from_N[n]))
        lst.append(-1 if ans == Inf else ans)
    print(*lst)


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

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, M, U, V)


if __name__ == "__main__":
    main()
