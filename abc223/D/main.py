#!/usr/bin/env python3

from collections import defaultdict

def main2():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    mp = map(int, sys.stdin.read().split())
    E = [(a - 1, b - 1) for a, b in zip(mp, mp)]
    ans, _ = topological_sort_kahn_pqueue(N, E)
    if len(ans) != N:
        print(-1)
    else:
        print(*[i + 1 for i in ans])


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    ans, _ = topological_sort_kahn_pqueue(N, [(a - 1, b - 1) for a, b in zip(A, B)])
    if len(ans) != N:
        return None
    else:
        return [i + 1 for i in ans]


def topological_sort_kahn_pqueue(N, E: "List[Tuple[int, int]]") -> "Tuple[List[int], bool]":
    """「Kahnのアルゴリズム」でheapqを適用したもの。辞書順になる"""
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

def main():
    import sys

    sys.setrecursionlimit(10**5)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    ans = solve(N, M, A, B)
    if ans:
        print(*ans)
    else:
        print(-1)


def solve_slow(N, M, A, B):
    import itertools
    links = defaultdict(set)
    for a, b in zip(A, B):
        links[b].add(a)
    before = defaultdict(set)
    for n in range(1, N + 1):
        visited = set()
        to_visit = [n]
        while to_visit:
            u = to_visit.pop()
            if u in visited:
                continue
            visited.add(u)
            for v in links[u]:
                before[n].add(v)
                to_visit.append(v)

    for tup in itertools.permutations(range(1, N + 1)):
        ok = True
        shown = set()
        for v in tup:
            if before[v] - shown:
                ok = False
                break
            shown.add(v)
        if ok:
            return list(tup)
    return None


def _debug():
    import random
    while True:
        N = 10
        M = 10
        A, B = [], []
        for _ in range(M):
            a, b = random.sample(range(1, N + 1), 2)
            A.append(a)
            B.append(b)

        ans = solve(N, M, A, B)
        ans2 = solve_slow(N, M, A, B)
        if ans != ans2:
            print(f"N: {N}, M: {M}, AB: {list(zip(A, B))}")
            print("expected", ans2)
            print("actual  ", ans)
            print("--")
            print(f"{N} {M}")
            for a, b in zip(A, B):
                print(a, b)
        break


if __name__ == "__main__":
    # _debug()
    # main()
    main2()
