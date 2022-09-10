#!/usr/bin/env python3
from collections import defaultdict


def main():
    """初AC https://atcoder.jp/contests/abc197/submissions/34682096
    「同じ色のグループについて左端と右端だけ考えれば良い」というところまでは解説と同じ
    ダイクストラはややオーバーキルだった感じ。実装も不必要に込み入ってしまった

    - 出発点をindex 0のノードとする
    - 同じグループについて、ボールが1つならそれをそのままノードとみなして、前後のグループと繋げる
    - ノードが2つ以上あるなら、左端と右端についてノードを2つ用意する（入り口と出口）
    - 左端入り口ノードと右端出口ノード、右端入り口ノードと左端出口ノードをつなげる
    - 入り口ノードと出口ノードをそれぞれ前後のグループとつなげる
    - ここまでの総ノード数に加えて、ゴールとなる座標 0 のノードを更に一つ用意する
    - 以上で出来たグラフをダイクストラ法で解くと、出発点からゴールまでのコストが答え
    """
    import sys
    input = sys.stdin.readline
    N = int(input())
    X, C = [0] * N, [0] * N
    for i in range(N):
        X[i], C[i] = map(int, input().split())

    cx = defaultdict(list)
    for n, (x, c) in enumerate(zip(X, C), start=1):
        cx[c].append((x, n))

    # 0 -> N + 1
    cn = [[(0, 0)]]
    for c in sorted(cx.keys()):
        if len(cx[c]) == 1:
            cn.append([cx[c][0]])
        else:
            cx[c].sort()
            cn.append([cx[c][0], cx[c][-1]])
    cn.append([(0, N + 1)])
    del cx  # 予防

    num_nodes = 0
    E = defaultdict(list)
    for i, nodes in enumerate(cn[:-1]):
        assert len(nodes) in [1, 2]
        next_nodes = cn[i + 1]
        if len(nodes) == 1:
            src = nodes[0][0]
            for j, (dst, _) in enumerate(next_nodes):
                E[num_nodes].append((abs(dst - src), num_nodes + 1 + j))
            num_nodes += 1
        else:
            x_min, _ = nodes[0]
            x_max, _ = nodes[1]
            E[num_nodes].append((abs(x_max - x_min), num_nodes + 3))
            E[num_nodes + 1].append((abs(x_max - x_min), num_nodes + 2))
            for j, (dst, _) in enumerate(next_nodes):
                E[num_nodes + 2].append((abs(dst - x_min), num_nodes + 4 + j))
                E[num_nodes + 3].append((abs(dst - x_max), num_nodes + 4 + j))
            num_nodes += 4
    num_nodes += 1
    # print(E)
    dijkstra = Dijkstra(N=num_nodes, E=E)
    lst = dijkstra.solve(0)
    ans = lst[num_nodes - 1]
    print(ans)


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


if __name__ == "__main__":
    main()
