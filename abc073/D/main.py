#!/usr/bin/env python3

import itertools
from collections import defaultdict

Inf = INF = float("INF")


def solve(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    E = defaultdict(list)
    for a, b, c in zip(A, B, C):
        a -= 1
        b -= 1
        E[a].append((c, b))
        E[b].append((c, a))

    dijkstra = Dijkstra(N, E)
    d = [[Inf] * R for _ in range(R)]
    for i, r0 in enumerate(r):
        r0 -= 1
        lst = dijkstra.solve(r0)
        for j, r1 in enumerate(r):
            r1 -= 1
            d[i][j] = lst[r1]
    # for i in range(R):
    #     for j in range(R):
    #         assert d[i][j] == d[j][i]

    # ans = Inf
    # for perm in itertools.permutations(range(R)):
    #     ans = min(ans, sum(d[perm[i]][perm[i + 1]] for i in range(R - 1)))
    # print(ans)

    # んーなんでかなWA
    dp = [Inf] * (1 << R)
    dp[(1 << R) - 1] = 0
    for S in range((1 << R) - 2, -1, -1):
        for u in range(R):
            if not ((S >> u) & 1):
                continue
            for v in range(R):
                if (S >> v) & 1:
                    continue
                dp[S] = min(dp[S], dp[S | (1 << v)] + d[u][v])
    print(min(dp[1 << i] for i in range(R)))


def solve_dj(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    # 前半はワーシャルフロイドでも(R回の)ダイクストラでも良い
    E = defaultdict(list)
    for a, b, c in zip(A, B, C):
        a -= 1
        b -= 1
        E[a].append((c, b))
        E[b].append((c, a))

    dijkstra = Dijkstra(N, E)
    d = [[Inf] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for r0 in r:
        r0 -= 1
        d[r0] = dijkstra.solve(r0)

    ans = Inf
    for perm in itertools.permutations(r0 - 1 for r0 in r):
        ans = min(ans, sum(d[perm[i]][perm[i + 1]] for i in range(R - 1)))
    print(ans)



def solve_ref(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    d = [[Inf] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for a, b, c in zip(A, B, C):
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c
    for m in range(N):
        for u in range(N):
            for v in range(N):
                d[u][v] = min(d[u][v], d[u][m] + d[m][v])

    ans = Inf
    for perm in itertools.permutations(r0 - 1 for r0 in r):
        ans = min(ans, sum(d[perm[i]][perm[i + 1]] for i in range(R - 1)))
    print(ans)


def solve_wa(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    E = defaultdict(list)
    for a, b, c in zip(A, B, C):
        a -= 1
        b -= 1
        E[a].append((c, b))
        E[b].append((c, a))

    dijkstra = Dijkstra(N, E)
    d = [[Inf] * R for _ in range(R)]
    for i, r0 in enumerate(r):
        r0 -= 1
        lst = dijkstra.solve(r0)
        for j, r1 in enumerate(r):
            r1 -= 1
            d[i][j] = lst[r1]
    # ↑ ここまでは合ってる模様

    # ↓ TSPの勉強直後でDPを使っているが、permutationsで全通り試すのが正しかった
    dp = [Inf] * (1 << R)
    dp[(1 << R) - 1] = 0
    for S in range((1 << R) - 2, -1, -1):
        for u in range(R):
            if not S >> u & 1:
                continue
            for v in range(R):
                if u == v or ((S >> v) & 1):
                    continue
                # print(format(S, "b").zfill(R), format(S | 1 << v, "b").zfill(R), "",
                #       u, v, "", dp[S], dp[S | 1 << v], "+", d[u][v], "", min(dp[S], dp[S | 1 << v] + d[u][v]))
                dp[S] = min(dp[S], dp[S | 1 << v] + d[u][v])
    # print(d)
    # print(dp)
    print(min(dp[1 << i] for i in range(R)))


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


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    r = [int(next(tokens)) for _ in range(R)]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, R, r, A, B, C)


if __name__ == "__main__":
    main()
