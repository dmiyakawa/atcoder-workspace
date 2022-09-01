#!/usr/bin/env python3

"""トポロジカルソート
DAGの並び替え
"""
from collections import defaultdict, deque


def topological_sort_bfs(N, links) -> "List[int]":
    """NノードのDAGに対して幅優先探索を用いたトポロジカルソートを行う。ノード番号は[0, N-1]"""
    # https://onlinejudge.u-aizu.ac.jp/status/users/dmiyakawa/submissions/1/GRL_4_B/judge/6905079/Python3
    visited = [False] * N
    indeg = [0] * N
    out = []

    def bfs(s):
        q = deque()
        q.append(s)
        visited[s] = True
        while q:
            _u = q.popleft()
            out.append(_u)
            for _v in links[_u]:
                indeg[_v] -= 1
                if indeg[_v] == 0 and not visited[_v]:
                    visited[_v] = True
                    q.append(_v)

    for u in range(N):
        for v in links[u]:
            indeg[v] += 1
    for u in range(N):
        if indeg[u] == 0 and not visited[u]:
            bfs(u)
    return out


def topological_sort_kahn(N, E: "List[Tuple[int, int]]") -> "Tuple[List[int], bool]":
    """トポロジカルソートの結果と、その結果が一意であるかを示すフラグをタプルで返す。
    ノード番号は [0, N-1]
    「Kahnのアルゴリズム」と呼ばれるアルゴリズム
    """
    from collections import deque

    G = [[] for _ in range(N)]
    C = [0] * N

    for i, j in E:
        G[i] += j,
        C[j] += 1

    q = deque(i for i in range(N) if not C[i])
    is_unique = True
    ans = []
    while q:
        if 1 < len(q):
            is_unique = False
        i = q.popleft()
        ans.append(i)
        for j in G[i]:
            C[j] -= 1
            if not C[j]:
                q += j,
    return ans, is_unique


def topological_sort_kahn_pqueue(N, E: "List[Tuple[int, int]]") -> "Tuple[List[int], bool]":
    """「Kahnのアルゴリズム」でheapqを適用したもの。辞書順になる
    WIP"""
    import heapq

    G = [[] for _ in range(N)]
    C = [0] * N

    for i, j in E:
        G[i] += j,
        C[j] += 1

    hq = []
    for i in range(N):
        if C[i]:
            continue
        heapq.heappush(hq, i)
    # q = deque(i for i in range(N) if not C[i])
    is_unique = True
    ans = []
    while hq:
        if 1 < len(hq):
            is_unique = False
        # i = q.popleft()
        i = heapq.heappop(hq)
        ans.append(i)
        for j in G[i]:
            C[j] -= 1
            if not C[j]:
                heapq.heappush(hq, j)
                # q += j,
    return ans, is_unique





def topological_sort_dfs(N, links) -> "List[int]":
    """NノードのDAGに対して深さ優先探索を用いたトポロジカルソートを行う。ノード番号は[0, N-1]"""
    # https://onlinejudge.u-aizu.ac.jp/status/users/dmiyakawa/submissions/1/GRL_4_B/judge/6905187/Python3
    visited = [False] * N
    out = []

    def dfs(_u):
        visited[_u] = True
        for _v in links[_u]:
            if not visited[_v]:
                dfs(_v)
        out.append(_u)

    for u in range(N):
        if not visited[u]:
            dfs(u)
    out.reverse()
    return out


def grl_4_b():
    """https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_B"""
    V, E = map(int, input().split())
    # ノード番号は 0, ... V-1
    links = defaultdict(list)
    for _ in range(E):
        s, t = map(int, input().split())
        links[s].append(t)
    # out = topological_sort_bfs(V, links)
    out = topological_sort_dfs(V, links)
    # print(out)
    for v in out:
        print(v)


def abc223_d():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    mp = map(int, sys.stdin.read().split())
    E = [(a - 1, b - 1) for a, b in zip(mp, mp)]
    ans, _ = topological_sort_kahn_pqueue(N, E)
    if len(ans) != N:
        print(-1)
    else:
        print(*[i + 1 for i in ans])


if __name__ == "__main__":
    abc223_d()
    # grl_4_b()
