#!/usr/bin/env python3

from collections import deque, defaultdict
from typing import NamedTuple, Optional, List, cast


def main_ref():
    """https://atcoder.jp/contests/abc274/editorial/5098"""
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]
    vg = [[-1] * W for _ in range(H)]
    hg = [[-1] * W for _ in range(H)]
    nh, nv = -1, -1
    for h in range(H):
        seq = False
        for w in range(W):
            if grid[h][w] == "#":
                seq = False
                continue
            if not seq:
                seq = True
                nh += 1
            vg[h][w] = nh
    nh += 1
    # for h in range(H):
    #     print("".join(f"{vg[h][w]:02x}" if vg[h][w] >= 0 else "##" for w in range(W)))

    d = defaultdict(set)
    for w in range(W):
        seq = False
        for h in range(H):
            if grid[h][w] == "#":
                seq = False
                continue
            if not seq:
                seq = True
                nv += 1
            hg[h][w] = nv
            if vg[h][w] >= 0:
                d[vg[h][w]].add(nv)
    # print()
    # for h in range(H):
    #     print("".join(f"{hg[h][w]:02x}" if hg[h][w] >= 0 else "##" for w in range(W)))
    nv += 1
    N = nh + nv + 2
    # gr = MFGraph(N)  # Dinic(N)
    gr = Dinic(N)
    for i in range(nh):
        # print(0, 1 + i, 1)
        gr.add_edge(0, 1 + i, 1)
    # for h in range(H):
    #     for w in range(W):
    #         if grid[h][w] == ".":
    #             gr.add_edge(1 + vg[h][w], 1 + nh + hg[h][w], 1)
    for fr, s in d.items():
        for to in s:
            # print(1 + fr, 1 + nh + to, 1)
            gr.add_edge(1 + fr, 1 + nh + to, 1)
    for i in range(nv):
        # print(1 + nh + i, N - 1, 1)
        gr.add_edge(1 + nh + i, N - 1, 1)
    print(gr.flow(0, N - 1))


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
            self.rev: "Optional[MFGraph._Edge]" = None

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
        """\
        頂点 s から t へ流せる限り流し、流せた量を返す。
        flow_limitが指定された場合はその量に達するまで流せる限り流し、流せた量を返す

        mを追加された辺数として
        - 辺の容量がすべて 1 のとき O(min(n^3/2, m^3/2))
        - O(n^2 m)
        """
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


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


if __name__ == "__main__":
    main_ref()
