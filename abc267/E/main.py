#!/usr/bin/env python3
import heapq
from collections import defaultdict


def solve(N: int, M: int, A: "List[int]", U: "List[int]", V: "List[int]"):
    links = defaultdict(set)
    costs = [0] * N
    for u, v in zip(U, V):
        u -= 1
        v -= 1
        links[u].add(v)
        links[v].add(u)
        costs[u] += A[v]
        costs[v] += A[u]

    q = [(c, i) for i, c in enumerate(costs)]

    heapq.heapify(q)
    ans = 0
    visited = set()
    while q:
        _, u = heapq.heappop(q)
        if u in visited:
            continue
        visited.add(u)
        ans = max(ans, costs[u])
        for v in links[u]:
            if v in visited:
                continue
            costs[v] -= A[u]
            links[v].remove(u)
            heapq.heappush(q, (costs[v], v))
        del links[u]
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, M, A, U, V)


if __name__ == "__main__":
    main()
