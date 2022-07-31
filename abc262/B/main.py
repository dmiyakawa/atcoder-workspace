#!/usr/bin/env python3

import sys
from collections import defaultdict

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, U: "List[int]", V: "List[int]"):
    links = defaultdict(list)
    for u, v in zip(U, V):
        links[u].append(v)
        links[v].append(u)
    s = set()
    for src, dests in links.items():
        N = len(dests)
        for i in range(N):
            for j in range(i + 1, N):
                if dests[i] not in links[dests[j]]:
                    continue
                if dests[i] < src < dests[j]:
                    s.add((dests[i], src, dests[j]))
                elif dests[j] < src < dests[i]:
                    s.add((dests[j], src, dests[i]))

    print(len(s))


def main():

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
    solve(N, M, U, V)


if __name__ == "__main__":
    main()
