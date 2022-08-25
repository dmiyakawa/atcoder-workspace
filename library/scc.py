class SCCGraph:
    """\
    強連結成分 (Strongly Connected Component)とそれらを結ぶDAGを管理するクラス
    Reference: R. Tarjan, Depth-First Search and Linear Graph Algorithms
    """

    def __init__(self, n: int = 0) -> None:
        from collections import namedtuple

        self._n = n
        self._edges: "List[Tuple[int, int]]" = []
        self._CSR = namedtuple("CSR", ["start", "elist"])

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """ならし O(1)"""
        n = self.num_vertices()
        assert 0 <= from_vertex < n
        assert 0 <= to_vertex < n
        self._edges.append((from_vertex, to_vertex))

    def scc(self) -> "List[List[int]]":
        """\
        SCCそれぞれをリストとし、またそれらをノードと見立ててトポロジカルソートした結果を返す。
        追加した本数を m として O(n + m)
        """
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: "List[List[int]]" = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups

    def num_vertices(self) -> int:
        return self._n

    def scc_ids(self) -> "Tuple[int, List[int]]":
        import sys

        def make_csr(n: int, edges: "List[Tuple[int, int]]"):
            _start = [0] * (n + 1)
            _elist = [0] * len(edges)

            for e in edges:
                _start[e[0] + 1] += 1

            for i in range(1, n + 1):
                _start[i] += _start[i - 1]

            counter = _start.copy()
            for e in edges:
                _elist[counter[e[0]]] = e[1]
                counter[e[0]] += 1
            return self._CSR(_start, _elist)

        g = make_csr(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids
