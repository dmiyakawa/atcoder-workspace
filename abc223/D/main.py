#!/usr/bin/env python3

from collections import defaultdict


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    links = defaultdict(set)
    for a, b in zip(A, B):
        links[b].add(a)

    seen = [False] * (N + 1)
    finished = [False] * (N + 1)

    def detect_loop_dfs(u) -> bool:
        nonlocal seen, finished
        seen[u] = True
        for v in links[u]:
            if finished[v]:
                continue
            if seen[v] and not finished[v]:
                return True
            if detect_loop_dfs(v):
                return True
        finished[u] = True
        return False

    for n in range(1, N + 1):
        if finished[n]:
            continue
        if detect_loop_dfs(n):
            print(-1)
            return

    used = set()
    lst = []

    def traverse(_u):
        if _u in used:
            return
        used.add(_u)
        if links[_u]:
            for _v in sorted(links[_u]):
                traverse(_v)
        lst.append(_u)


    for n in range(1, N + 1):
        traverse(n)

    print(*lst)


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
    solve(N, M, A, B)


if __name__ == "__main__":
    main()
