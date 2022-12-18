#!/usr/bin/env python3
from collections import defaultdict


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    E = defaultdict(list)
    for h in range(H):
        for w in range(W):
            dp = [[0] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    h0, w0 = h + i, w + j
                    if h0 >= H or w0 >= W or (i, j) in {(0, 0), (2, 2)}:
                        continue
                    if S[h0][w0] == "#":
                        cost = 1
                    else:
                        if i > 0:
                            a = 1 if S[h0-1][w0] == "#" else dp[i-1][j]
                        else:
                            a = 0
                        if j > 0:
                            b = 1 if S[h0][w0-1] == "#" else dp[i][j-1]
                        else:
                            b = 0
                        cost = min(a, b)
                    dp[i][j] = cost
                    u = h*W+w
                    v = h0*W+w0
                    E[u].append((cost, v))
                    E[v].append((cost, u))
    dk = Dijkstra(H*W, E)
    lst = dk.solve(0)
    from pprint import pprint
    pprint(dict(E))
    print(lst)
    print(lst[-1])



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


if __name__ == "__main__":
    main()
