#!/usr/bin/env python3

import sys
from collections import defaultdict

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, C: "List[int]", A: "List[int]", B: "List[int]"):
    E = defaultdict(set)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        E[a].add(b)
        E[b].add(a)

    good = [True] * N
    cs = {}
    visited = set()

    def _dfs(u):
        if u in visited:
            return
        visited.add(u)
        if cs.get(C[u], 0) > 0:
            good[u] = False

        cs[C[u]] = cs.get(C[u], 0) + 1
        for v in E[u]:
            if v in visited:
                continue
            _dfs(v)
        cs[C[u]] -= 1

    _dfs(0)

    for i, g in enumerate(good):
        if g:
            print(i + 1)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, C, A, B)


if __name__ == "__main__":
    main()
