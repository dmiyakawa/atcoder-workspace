#!/usr/bin/env python3

from collections import defaultdict


def solve(N: int, M: int, U: "List[int]", V: "List[int]"):
    """初AC。この解説と同じ https://atcoder.jp/contests/abc245/editorial/3667"""
    flinks = defaultdict(set)
    blinks = defaultdict(set)
    to_check = {n for n in range(N)}
    ans = {n for n in range(N)}
    for u, v in zip(U, V):
        u -= 1
        v -= 1
        flinks[u].add(v)
        blinks[v].add(u)
        to_check.discard(u)
    while to_check:
        v = to_check.pop()
        ans.discard(v)
        for u in blinks[v]:
            flinks[u].discard(v)
            if not flinks[u]:
                to_check.add(u)
    print(len(ans))


def solve_ref(N, M, U, V):
    """SCC + DP
    https://atcoder.jp/contests/abc245/editorial/3664
    トポロジカルソートの結果では順序は決まるが本問の求める「たどり着けるか」の判定は出来ない。
    強連結成分への依存関係がないノードもソート結果のDAGには乗っているため。
    そのため、後半でトポロジカルソート結果の後ろからDPを行う。
    自分自身が複数要素を含むSCCならそのdp[i]はTrueで問題ない
    単独要素なら、そのノードから直接辿れるノードjのdp[j]がTrueであるのが必要十分条件
    （ソート結果の後ろからたどっているので後段のノードのdp[j]は準備済のはず）
    """
    g = SCCGraph(N)
    links = defaultdict(set)
    for u, v in zip(U, V):
        u -= 1
        v -= 1
        g.add_edge(u, v)
        links[u].add(v)

    scc = g.scc()
    k = len(scc)
    idx = [0] * N
    for i, lst in enumerate(scc):
        for j in lst:
            idx[j] = i

    dp = [0] * k
    ans = 0
    for i in range(k - 1, -1, -1):
        if len(scc[i]) == 1:
            for v in links[scc[i][0]]:
                dp[i] |= dp[idx[v]]
        else:
            dp[i] = 1
        if dp[i]:
            ans += len(scc[i])
    print(ans)


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


def solve_tle(N: int, M: int, U: "List[int]", V: "List[int]"):
    links = defaultdict(list)
    for u, v in zip(U, V):
        links[u - 1].append(v - 1)
    ans_set = set()
    to_visit = {n for n in range(N)}
    while to_visit:
        n = to_visit.pop()

        in_stack = set()

        def dfs(_u):
            to_visit.discard(_u)
            if _u in ans_set or _u in in_stack:
                return True
            in_stack.add(_u)
            ret = False
            for _v in links[_u]:
                ret = ret or dfs(_v)
            if ret:
                ans_set.add(_u)
            in_stack.remove(_u)
            return ret

        dfs(n)
    print(len(ans_set))


def main():
    import sys

    sys.setrecursionlimit(10**8)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve_ref(N, M, U, V)


if __name__ == "__main__":
    main()
