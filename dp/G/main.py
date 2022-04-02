#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)


def solve(N: int, M: int, X: "List[int]", Y: "List[int]"):
    links = {}
    for x, y in zip(X, Y):
        links.setdefault(x - 1, set()).add(y - 1)

    lens = [0] * N
    visited = [False] * N

    def get_length(node_i):
        if visited[node_i]:
            return lens[node_i]
        next_nodes = links.get(node_i, set())
        if next_nodes:
            l = max(get_length(next_node_i) for next_node_i in next_nodes) + 1
        else:
            l = 0
        visited[node_i] = True
        lens[node_i] = l
        return l

    max_len = 0
    for i in range(N):
        max_len = max(get_length(i), max_len)

    print(max_len)


if __name__ == "__main__":
    main()
