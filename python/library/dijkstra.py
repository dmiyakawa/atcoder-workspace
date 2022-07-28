#!/usr/bin/env python3
#
# 無向グラフ型ダイクストラ
#
# https://atcoder.jp/contests/typical90/tasks/typical90_m
#


class Dijkstra:
    def __init__(self, N: int, E: "Dict[int, List[Tuple[float, int]]]", inf=float("inf")):
        self.N = N
        # (cost, dest) のリスト
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


class DijkstraP:
    """バックトラック用のノード番号が返されるバージョン"""
    def __init__(self, N: int, E: "Dict[int, List[Tuple[float, int]]]", inf=float("inf")):
        """\n
        :param N: ノード数
        :param E: エッジに関する情報。ただしノード番号は0〜N-1
        :param inf: 到達できない際の無限大のコスト
        """
        self.N = N
        self.E = E
        self.inf = inf

    def solve(self, start: int) -> "Tuple[List[float], List[int]]":
        """"""
        import heapq

        costs: "List[float]" = [self.inf] * self.N
        prevs: "List[int]" = [-1] * self.N
        costs[start] = 0
        h: "List[Tuple[float, int]]" = [(0, start)]
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
                    heapq.heappush(h, (costs[dest], dest))  # type: ignore
        return costs, prevs


def abc252_e():
    """https://atcoder.jp/contests/abc252/tasks/abc252_e"""
    from collections import defaultdict
    E = defaultdict(list)
    links: "Dict[Tuple[int, int], int]" = {}
    N, M = map(int, input().split())
    for i in range(M):
        a, b, c = [int(e) - 1 for e in input().split()]
        E[a].append((c, b))
        E[b].append((c, a))
        links[(a, b)] = i
    di = DijkstraP(N, E)
    costs, prevs = di.solve(0)
    print(*[links[tuple(sorted([i, j]))] for i, j in enumerate(prevs[1:], start=1)])  # type: ignore


if __name__ == "__main__":
    abc252_e()
