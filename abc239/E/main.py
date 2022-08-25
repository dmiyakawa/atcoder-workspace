#!/usr/bin/env python3

from collections import defaultdict

def solve(N: int, Q: int, X: "List[int]", A: "List[int]", B: "List[int]", V: "List[int]", K: "List[int]"):

    links = defaultdict(list)
    for a, b in zip(A, B):
        a -= 1
        b -= 1
        links[a].append(b)
        links[b].append(a)

    d = {}
    visited = set()

    def dfs(n):
        visited.add(n)

        lst = [X[n]]
        for link in links[n]:
            if link in visited:
                continue
            lst.extend(dfs(link))

        lst.sort(reverse=True)
        lst = lst[:20]
        d[n] = lst
        return lst

    dfs(0)
    # print(d)

    for v, k in zip(V, K):
        print(d[v - 1][k - 1])


def main():
    import sys

    sys.setrecursionlimit(10**9)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    V = [int()] * (Q)  # type: "List[int]"
    K = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        V[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, Q, X, A, B, V, K)


if __name__ == "__main__":
    main()
