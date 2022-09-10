#!/usr/bin/env python3
from collections import defaultdict, deque

MOD = 1000000007  # type: int


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    links = defaultdict(set)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        links[a].add(b)
        links[b].add(a)

    dp = [{} for _ in range(N)]
    dp[0][0] = 1
    to_visit = deque([(0, 0)])
    visited = set()
    while to_visit:
        u, c = to_visit.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in links[u]:
            dp[v][c + 1] = (dp[v].get(c + 1, 0) + dp[u][c]) % MOD
            links[v].remove(u)
            to_visit.appendleft((v, c + 1))
        del links[u]
    d = dp[N - 1]
    if d:
        print(d[min(d.keys())] % MOD)
    else:
        print(0)


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
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == "__main__":
    main()
