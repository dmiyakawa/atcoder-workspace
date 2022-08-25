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

import sys

input = sys.stdin.readline

N = int(input())  # 1 <= N <= 5000
M = int(input())  # 1 <= M <= 100,000
lst = [tuple(int(e) for e in input().split()) for _ in range(M)]
ans, is_unique = tsort_2(N, lst)
print(*ans, "0" if is_unique else "1", sep="\n")
