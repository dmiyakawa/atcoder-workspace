#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    Q = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, D, Q, P)


def solve(N: int, D: "List[List[int]]", Q: int, P: "List[int]"):
    import copy
    S = copy.copy(D)
    for i in range(N):
        for j in range(N):
            S[i][j] += ((S[i - 1][j] if i > 0 else 0)
                        + (S[i][j - 1] if j > 0 else 0)
                        - (S[i - 1][j - 1] if i > 0 and j > 0 else 0))
    # for s in S:
    #     print(s)

    for p in P:  # O(N^2)
        ans = 0
        for h in range(1, min(p, N) + 1):  # O(N)
            w = min(p // h, N)
            # print(f" {h}x{w}")
            for i in range(N - h + 1):  # O(N)
                for j in range(N - w + 1):  # O(N)
                    val = (S[i + h - 1][j + w - 1]
                           - (S[i - 1][j + w - 1] if i > 0 else 0)
                           - (S[i + h - 1][j - 1] if j > 0 else 0)
                           + (S[i - 1][j - 1] if i > 0 and j > 0 else 0))
                    # print(f" p:{p} h:{h} w:{w} i:{i} j:{j} -> val:{val}")
                    ans = max(ans, val)
        print(ans)


if __name__ == "__main__":
    main()
