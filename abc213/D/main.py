#!/usr/bin/env python3

import sys
from collections import defaultdict

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]", B: "List[int]"):
    links = defaultdict(list)
    for a, b in zip(A, B):
        links[a].append(b)
        links[b].append(a)

    lst = []

    def dfs(u, p):
        lst.append(u)
        for v in sorted(links[u]):
            if v == p:
                continue
            dfs(v, u)
            lst.append(u)

    dfs(1, None)
    print(*lst)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == "__main__":
    main()
