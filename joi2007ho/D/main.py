#!/usr/bin/env python3
from collections import defaultdict
import sys

input = sys.stdin.readline

def solve_3(N, M, lst):
    ans, is_unique = tsort_2(N, lst)
    print(*ans, "0" if is_unique else "1", sep="\n")


def tsort_2(N, E: "List[Tuple[int, int]]") -> "Tuple[List[int], bool]":
    """トポロジカルソートの結果と、その結果が一意であるかを示すフラグをタプルで返す。ノード番号は [0, N-1]"""
    from collections import deque

    G = [[] for _ in range(N)]
    C = [0] * N

    for i, j in E:
        G[i - 1] += j - 1,
        C[j - 1] += 1

    q = deque(i for i in range(N) if not C[i])
    is_unique = True
    ans = []
    while q:
        if 1 < len(q):
            is_unique = False
        i = q.popleft()
        ans.append(i + 1)
        for j in G[i]:
            C[j] -= 1
            if not C[j]:
                q += j,
    return ans, is_unique



def solve_2(N, M, lst):
    """初AC。BFSベースのトポロジカルソートに小細工をしたもの"""
    from collections import deque
    links = defaultdict(list)
    for w, l in lst:
        links[w].append(l)

    visited = [False] * (N + 1)
    indeg = [0] * (N + 1)
    out = []

    def bfs(s):
        q = deque()
        q.append((s, 0))
        visited[s] = True
        while q:
            _u, _depth = q.popleft()
            out.append((_u, _depth))
            for _v in links[_u]:
                indeg[_v] -= 1
                if indeg[_v] == 0 and not visited[_v]:
                    visited[_v] = True
                    q.append((_v, _depth + 1))

    for u in range(1, N + 1):
        for v in links[u]:
            indeg[v] += 1
    for u in range(1, N + 1):
        if indeg[u] == 0 and not visited[u]:
            bfs(u)
    prev_depth = -1
    dup = False
    for v, depth in out:
        if depth == prev_depth:
            dup = True
        prev_depth = depth
        print(v)
    print(1 if dup else 0)


def solve_tle(N, M, lst):
    """初期実装。子要素で同じものを巡回してしまい、TLEになる"""
    non_losers = set(n for n in range(1, N + 1))
    links = defaultdict(set)
    for w, l in lst:
        links[w].add(l)
        non_losers.discard(l)
    ranks = {n: 1 for n in range(1, N + 1)}
    depth = 1
    parents = non_losers
    while parents:
        next_parents = set()
        for parent in parents:
            ranks[parent] = depth
            for loser in links[parent]:
                next_parents.add(loser)
        parents = next_parents
        depth += 1
    prev_rank = 0
    dup = False
    ans_lst = []
    for rank, n in sorted((rank, n) for n, rank in ranks.items()):
        if prev_rank == rank:
            dup = True
        ans_lst.append(n)
        prev_rank = rank
    for ans in ans_lst:
        print(ans)
    print(1 if dup else 0)



def main():
    N = int(input())  # 1 <= N <= 5000
    M = int(input())  # 1 <= M <= 100,000
    # 全ての 1 <= a < b <= n について a 位のチームと b 位のチームの試合で必ず a 位のチームが勝利した．
    lst = [tuple(int(e) for e in input().split()) for _ in range(M)]
    # output
    # - 1 行目からn行目までの n 行には，伝えられた情報に適合する順位表
    # - n + 1 行目には，出力した順位表以外に，伝えられた情報に適合する順位表が存在するかどうかを表す整数 (1 / 0)
    solve_3(N, M, lst)
    # solve_2(N, M, lst)
    # solve_tle(N, M, lst)


def main_ref():
    """https://atcoder.jp/contests/joi2007ho/submissions/31602623"""
    (n,), (m,), *E = [[*map(int, r.split())] for r in open(0)]
    G = [[] for _ in [0] * n]
    C = [0] * n

    for i, j in E:
        G[i - 1] += j - 1,
        C[j - 1] += 1

    q = [i for i in range(n) if not C[i]]
    f = 0
    r = []

    while q:
        if 1 < len(q):
            f = 1
        i = q.pop(0)
        r += i + 1,
        for j in G[i]:
            C[j] -= 1
            if not C[j]:
                q += j,

    print(*r, f, sep='\n')


if __name__ == "__main__":
    main()
