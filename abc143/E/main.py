#!/usr/bin/env python3

from collections import defaultdict

Inf = float("inf")


def solve(N: int, M: int, L: int, A: "List[int]", B: "List[int]", C: "List[int]",
          Q: int, S: "List[int]", T: "List[int]"):
    links = defaultdict(set)

    d = [[Inf for _ in range(N)] for _ in range(N)]
    d2 = [[Inf for _ in range(N)] for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
        d2[i][i] = 0

    for a, b, c in zip(A, B, C):
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    for i in range(N):
        for j in range(i + 1, N):
            if d[i][j] <= L:
                d2[i][j] = 1
                d2[j][i] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j])
    # print(d)
    # print(d2)
    for s, t in zip(S, T):
        s -= 1
        t -= 1
        print(-1 if d2[s][t] == Inf else d2[s][t] - 1)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    s = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, M, L, A, B, C, Q, s, t)


if __name__ == "__main__":
    main()
