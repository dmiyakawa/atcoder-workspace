#!/usr/bin/env python3

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)


def solve(N: int, U: "List[int]", V: "List[int]", W: "List[int]"):
    links = defaultdict(set)
    costs = {}
    for u, v, w in zip(U, V, W):
        u -= 1
        v -= 1
        costs[(u, v)] = w
        costs[(v, u)] = w
        links[u].add(v)
        links[v].add(u)

    visited = set()
    to_visit = {(0, 0)}
    ans = [-1] * N
    while to_visit:
        u, cu = to_visit.pop()
        if u in visited:
            continue
        visited.add(u)
        ans[u] = cu
        for v in links[u]:
            if v in visited:
                continue
            cv = cu if costs[(u, v)] % 2 == 0 else (1 - cu)
            to_visit.add((v, cv))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
