#!/usr/bin/env python3

from collections import defaultdict, deque
from typing import List

Inf = 1<<30


def main():
    N, M, Q, K = map(int, input().split())
    a = [int(e) for e in input().split()]
    # defaultdictだとTLEしやすい
    # links = defaultdict(list)
    links: List[List[int]] = [[] for _ in range(N)]
    for _ in range(M):
        u, v = [int(e) - 1 for e in input().split()]
        links[u].append(v)
        links[v].append(u)

    # 注: N**5くらいのデータを管理する際に辞書や集合を使うとこの問題だとそれだけでTLEになることがある（安定しない）
    gas_d = {a0: [Inf for _ in range(N + 1)] for a0 in a}
    # gas_l = [[Inf for _ in range(N + 1)] for _ in range(K)]
    for i, a0 in enumerate(a):
        d = gas_d[a0]
        # d = gas_l[i]
        d[a0] = 0
        to_visit = deque()
        to_visit.append(a0)
        while to_visit:
            node = to_visit.popleft()
            cost = d[node]
            for next_node in links[node]:
                if d[next_node] == Inf:
                    d[next_node] = cost + 1
                    to_visit.append(next_node)

    for _ in range(Q):
        s, t = [int(e) - 1 for e in input().split()]
        print(min(gas_l[i][s] + gas_l[i][t] for i in range(K)))
        # print(min(gas_d[a0][s] + gas_d[a0][t] for a0 in a))


def main_a():
    # https://atcoder.jp/contests/past202112-open/submissions/32506517
    n, m, q, k = map(int, input().split())
    aa = list(map(int, input().split()))

    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    d = [[Inf] * (n + 1) for _ in range(k)]
    for i, a in enumerate(aa):
        d[i][a] = 0
        que = deque([(a, 0)])
        while que:
            x, c = que.popleft()
            for b in g[x]:
                if d[i][b] == Inf:
                    d[i][b] = c + 1
                    que.append((b, c + 1))

    for _ in range(q):
        s, t = map(int, input().split())
        ans = Inf
        for i in range(k):
            ans = min(ans, d[i][s] + d[i][t])
        print(ans)


def main_a2():
    # https://atcoder.jp/contests/past202112-open/submissions/31066389
    import sys
    readline = sys.stdin.readline

    n, m, Q, k = map(int, readline().split())
    *a, = map(int, readline().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, readline().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    from collections import deque
    def dfs(g, root):
        INF = 1 << 30
        d = [INF] * n
        d[root] = 0
        q = deque()
        q.append(root)
        while q:
            v = q.popleft()
            for c in g[v]:
                if d[c] == INF:
                    d[c] = d[v] + 1
                    q.append(c)
        return d

    dist = [dfs(g, ai - 1) for ai in a]
    for _ in range(Q):
        u, v = map(int, readline().split())
        u -= 1
        v -= 1
        ans = 1 << 30
        for d in dist:
            ans = min(ans, d[u] + d[v])
        print(ans)


if __name__ == "__main__":
    main_a2()
