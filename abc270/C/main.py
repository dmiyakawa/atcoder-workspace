#!/usr/bin/env python3
from collections import defaultdict

Inf = float("inf")

def solve(N: int, X: int, Y: int, U: "List[int]", V: "List[int]"):
    links = defaultdict(set)
    for u, v in zip(U, V):
        links[u].add(v)
        links[v].add(u)

    prevs = [-1] * (N + 1)
    visited = set()
    to_visit = [X]
    lst = []
    while to_visit:
        u = to_visit.pop()
        if u in visited:
            continue
        visited.add(u)
        if u == Y:
            while u != X:
                lst.append(u)
                u = prevs[u]
            lst.append(u)
            break

        for v in links[u]:
            if v in visited:
                continue
            prevs[v] = u
            to_visit.append(v)
    lst.reverse()
    print(*lst)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    U = [int()] * (N - 1)  # type: "List[int]"
    V = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, X, Y, U, V)


if __name__ == "__main__":
    main()
