#!/usr/bin/env python3
from collections import defaultdict


def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    """ワーシャルフロイドを使うまでもなかった"""
    E = defaultdict(list)
    for i in range(10):
        for j in range(10):
            E[i].append((c[i][j], j))
            E[j].append((c[j][i], i))
    dk = Dijkstra(10, E)
    counts = [0] * 10
    for i in range(H):
        for j in range(W):
            if A[i][j] >= 0:
                counts[A[i][j]] += 1
    ans = 0
    for i in range(10):
        costs = dk.solve(i)
        ans += counts[i] * costs[1]
    print(ans)


def solve_1(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    """初回AC
    公式解説だとワーシャルフロイドで全パターンを求めているが、
    この解法は「各数字から1に向かう最小コスト」を求めるために「1から各数字に向かう最小コスト」を使っている
    有向グラフを逆転させて1から出発したときのダイクストラの結果を使える（はず）
    """
    E = defaultdict(list)
    for i in range(10):
        for j in range(10):
            # 1からの各数字へのコストを答えに使うため、わざとコストを逆転させている
            E[i].append((c[j][i], j))
            E[j].append((c[i][j], i))
    dk = Dijkstra(10, E)
    costs = dk.solve(1)
    counts = [0] * 10
    for i in range(H):
        for j in range(W):
            if A[i][j] >= 0:
                counts[A[i][j]] += 1
    # print(costs)
    # print(counts)
    print(sum(cost * count for (cost, count) in zip(costs, counts)))



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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [[int(next(tokens)) for _ in range(9 + 1)] for _ in range(9 + 1)]  # type: "List[List[int]]"
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, c, A)


if __name__ == "__main__":
    main()
