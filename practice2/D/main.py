#!/usr/bin/env python3
#
# https://atcoder.jp/contests/practice2/tasks/practice2_d
#
# マス目をチェッカー板のように交互に2色に分け「最大二部マッチング問題」として解くことができる
# https://qiita.com/magurofly/items/bfaf6724418bfde86bd0
#
# https://atcoder.github.io/ac-library/production/document_ja/maxflow.html
#

from typing import NamedTuple, Optional, List, cast


class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(re.dst, e.dst, e.cap + re.cap, re.cap)

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited


def main():
    N, M = [int(e) for e in input().split()]
    S = [input() for _ in range(N)]

    mf_graph = MFGraph(N * M + 2)
    s = N * M
    t = N * M + 1
    for i in range(N):
        for j in range(M):
            if S[i][j] == "#":
                continue
            v = i * M + j
            if (i + j) % 2 == 1:
                # 奇数ノードからシンクへのエッジを張る
                mf_graph.add_edge(v, t, 1)
                continue

            # ソースから偶数ノードへのエッジを張る
            mf_graph.add_edge(s, v, 1)

            # 偶数ノードから上下左右の奇数ノードへのエッジを張る
            if i > 0 and S[i - 1][j] == ".":
                mf_graph.add_edge(v, (i - 1) * M + j, 1)
            if i < N - 1 and S[i + 1][j] == ".":
                mf_graph.add_edge(v, (i + 1) * M + j, 1)
            if j > 0 and S[i][j - 1] == ".":
                mf_graph.add_edge(v, i * M + j - 1, 1)
            if j < M - 1 and S[i][j + 1] == ".":
                mf_graph.add_edge(v, i * M + j + 1, 1)

    # 最大流問題を解く。辺の数がそのままタイル数に対応する
    print(mf_graph.flow(s, t))

    # 流れのある偶数ノードから奇数ノードへのエッジを取得し、
    # 問題のルールに従って><, v^ を書き込む
    grid = [list(line) for line in S]
    for edge in mf_graph.edges():
        if edge.src == s or edge.dst == t or edge.flow == 0:
            continue
        i0 = edge.src // M
        j0 = edge.src % M
        i1 = edge.dst // M
        j1 = edge.dst % M
        if i0 == i1 + 1:
            grid[i1][j1] = "v"
            grid[i0][j0] = "^"
        elif i0 + 1 == i1:
            grid[i0][j0] = "v"
            grid[i1][j1] = "^"
        elif j0 == j1 + 1:
            grid[i1][j1] = ">"
            grid[i0][j0] = "<"
        else:
            grid[i0][j0] = ">"
            grid[i1][j1] = "<"

    print("\n".join("".join(lst) for lst in grid))


if __name__ == "__main__":
    main()



