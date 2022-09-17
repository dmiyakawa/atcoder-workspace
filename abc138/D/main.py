#!/usr/bin/env python3
from collections import defaultdict


def solve_2(N: int, Q: int, A: "List[int]", B: "List[int]", P: "List[int]", X: "List[int]"):
    links = defaultdict(set)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        links[a].add(b)
        links[b].add(a)

    vs = [0] * N
    for p, x in zip(P, X):
        p -= 1
        vs[p] += x

    visited = set()
    to_visit = [(0, 0)]
    ans = [-1] * N
    while to_visit:
        u, value = to_visit.pop()
        if u in visited:
            continue
        visited.add(u)
        value += vs[u]
        ans[u] = value
        for v in links[u]:
            if v in visited:
                continue
            to_visit.append((v, value))
    print(*ans)


def solve(N: int, Q: int, A: "List[int]", B: "List[int]", P: "List[int]", X: "List[int]"):
    links = defaultdict(set)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        links[a].add(b)
        links[b].add(a)

    values = [0] * N
    for p, x in zip(P, X):
        p -= 1
        values[p] += x

    visited = set()
    to_visit = [(0, 0)]
    ans = [-1] * N
    while to_visit:
        u, value = to_visit.pop()
        if u in visited:
            continue
        visited.add(u)
        value += values[u]
        ans[u] = value
        for v in links[u]:
            if v not in visited:
                to_visit.append((v, value))
    print(*ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve_2(N, Q, a, b, p, x)


if __name__ == "__main__":
    main()
