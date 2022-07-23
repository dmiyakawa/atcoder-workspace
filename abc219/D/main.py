#!/usr/bin/env python3
from typing import List, Any


def solve_ref(N: int, X: int, Y: int, A: "List[int]", B: "List[int]"):
    # https://atcoder.jp/contests/abc219/submissions/33394746
    Inf = 400
    dp = [[[Inf] * (Y + 1) for i in range(X + 1)] for i in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        a, b = A[i], B[i]
        for j in range(X + 1):
            for k in range(Y + 1):
                if dp[i][j][k] == Inf:
                    continue
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                j0, k0 = min(j + a, X), min(k + b, Y)
                dp[i + 1][j0][k0] = min(dp[i + 1][j0][k0], dp[i][j][k] + 1)

    print(dp[-1][X][Y] if dp[-1][X][Y] != Inf else -1)


def count_one(a):
    ans = 0
    while a:
        ans += 1 if a & 1 else 0
        a = a >> 1
    return ans

def solve_wa2(N: int, X: int, Y: int, A: "List[int]", B: "List[int]"):
    M = 300
    dp = {(0, 0): {frozenset()}}
    min_count = N + 1
    for i, (a, b) in enumerate(zip(A, B)):
        lst: Any = list(dp.items())
        for (a0, b0), cands in lst:
            if a0 + a > M or b0 + b > M:
                continue
            s = dp.setdefault((a0 + a, b0 + b), set())
            for cand in cands:
                if (a, b) in cand:
                    continue
                new_cand = cand | {i}
                s.add(new_cand)
                if a0 + a >= X and b0 + b >= Y:
                    min_count = min(min_count, len(new_cand))
    # print(dp)
    print(min_count if min_count <= N else -1)


def solve_wa1(N: int, X: int, Y: int, A: "List[int]", B: "List[int]"):
    # TLE, WA。全然ダメ
    # O(NXY) のdp解法を目指したのは解説と同じ。ただ、3次元にしなかったことで妙なことになった
    M = 300
    dp = [[2**(N + 1) - 1 for _ in range(M + 1)] for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(N):
        for a in range(M + 1):
            for b in range(M + 1):
                a1, b1 = a + A[i], b + B[i]
                if a1 > M or b1 > M:
                    continue
                if (
                        (dp[a][b] & (2 << i) == 0)
                        and format(dp[a][b], "b").count("1") + 1 < format(dp[a1][b1], "b").count("1")
                ):
                    dp[a + A[i]][b + B[i]] = dp[a][b] | (2 << i)
    ans = min(format(dp[a][b], "b").count("1") for a in range(M + 1) for b in range(M + 1) if a >= X and b >= Y)
    print(ans if ans <= N else -1)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve_ref(N, X, Y, A, B)


if __name__ == "__main__":
    main()
