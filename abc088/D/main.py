#!/usr/bin/env python3
from collections import defaultdict


def main():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.extend(list(input()))
    E = defaultdict(list)

    for i in range(H * W):
        if S[i] == "#":
            continue
        h, w = divmod(i, W)
        if h > 0 and S[i - W] == ".":
            E[i].append((1, i - W))
        if w > 0 and S[i - 1] == ".":
            E[i].append((1, i - 1))
        if h < H - 1 and S[i + W] == ".":
            E[i].append((1, i + W))
        if w < W - 1 and S[i + 1] == ".":
            E[i].append((1, i + 1))
    costs, prevs = DijkstraP(H * W, E).solve(0)
    if costs[H * W - 1] == float("inf"):
        print(-1)
        return
    n = H * W - 1
    route = []
    while n >= 0:
        route.append(n)
        n = prevs[n]
    # print(route)
    in_route = set(route)
    print(sum(1 for i in range(H * W) if S[i] == "." and i not in in_route))


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


if __name__ == "__main__":
    main()
