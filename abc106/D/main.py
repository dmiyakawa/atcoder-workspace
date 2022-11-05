#!/usr/bin/env python3

import sys
from collections import defaultdict

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, Q: int, L: "List[int]", R: "List[int]", p: "List[int]", q: "List[int]"):
    lst_l = [0] * N
    lst_r = [0] * N
    dict_l = defaultdict(list)
    for l, r in zip(L, R):
        l -= 1
        r -= 1
        lst_l[l] += 1
        lst_r[r] += 1
        dict_l[l].append(r)

    dp = [[0] * N for _ in range(N)]
    dp[0][N - 1] = M
    for l in range(N):
        if l > 0:
            dp[l][N - 1] = dp[l - 1][N - 1] - lst_l[l - 1]
            for r in dict_l[l - 1]:
                lst_r[r] -= 1
        for r in range(N - 2, l - 1, -1):
            dp[l][r] = dp[l][r + 1] - lst_r[r + 1]
    for p0, q0 in zip(p, q):
        p0 -= 1
        q0 -= 1
        print(dp[p0][q0])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    q = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    solve(N, M, Q, L, R, p, q)


if __name__ == "__main__":
    main()
