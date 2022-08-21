#!/usr/bin/env python3

class TwoSAT:
    """
    2-SAT

    Reference:
    B. Aspvall, M. Plass, and R. Tarjan,
    A Linear-Time Algorithm for Testing the Truth of Certain Quantified Boolean
    Formulas
    """

    def __init__(self, n: int = 0) -> None:
        from collections import namedtuple
        self._n = n
        self._answer = [False] * n
        self._scc_n = 2 * n
        self._scc_edges: "List[Tuple[int, int]]" = []
        self._CSR = namedtuple("CSR", ["start", "elist"])

    def add_clause(self, i: int, f: bool, j: int, g: bool) -> None:
        assert 0 <= i < self._n
        assert 0 <= j < self._n

        self._scc_add_edge(2 * i + (0 if f else 1), 2 * j + (1 if g else 0))
        self._scc_add_edge(2 * j + (0 if g else 1), 2 * i + (1 if f else 0))

    def satisfiable(self) -> bool:
        scc_id = self._scc_ids()[1]
        for i in range(self._n):
            if scc_id[2 * i] == scc_id[2 * i + 1]:
                return False
            self._answer[i] = scc_id[2 * i] < scc_id[2 * i + 1]
        return True

    def answer(self) -> "List[bool]":
        return self._answer

    def _scc_add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """ならし O(1)"""
        assert 0 <= from_vertex < self._scc_n
        assert 0 <= to_vertex < self._scc_n
        self._scc_edges.append((from_vertex, to_vertex))

    def _scc_ids(self) -> "Tuple[int, List[int]]":
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

        g = make_csr(self._scc_n, self._scc_edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._scc_n
        order = [-1] * self._scc_n
        ids = [0] * self._scc_n

        sys.setrecursionlimit(max(self._scc_n + 1000, sys.getrecursionlimit()))

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
                    order[u] = self._scc_n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._scc_n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._scc_n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def _scc(self) -> "List[List[int]]":
        """\
        SCCそれぞれをリストとし、またそれらをノードと見立ててトポロジカルソートした結果を返す。
        追加した本数を m として O(n + m)
        """
        ids = self._scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: "List[List[int]]" = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups


def practice2_h():
    import sys

    input = sys.stdin.readline
    N, D = map(int, input().split())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ts = TwoSAT(N)
    for i in range(N):
        for j in range(i + 1, N):
            if abs(X[i] - X[j]) < D:
                ts.add_clause(i, False, j, False)
            if abs(X[i] - Y[j]) < D:
                ts.add_clause(i, False, j, True)
            if abs(Y[i] - X[j]) < D:
                ts.add_clause(i, True, j, False)
            if abs(Y[i] - Y[j]) < D:
                ts.add_clause(i, True, j, True)

    if not ts.satisfiable():
        print("No")
        return
    print("Yes")
    answer = ts.answer()
    for i in range(N):
        print(X[i] if answer[i] else Y[i])


if __name__ == "__main__":
    practice2_h()

