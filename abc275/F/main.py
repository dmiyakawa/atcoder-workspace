#!/usr/bin/env python3

"""
全体的に解説見てから解いている
https://atcoder.jp/contests/abc275/editorial/5140
"""

from typing import List


def solve(N: int, M: int, A: "List[int]"):
    inf = 10**9
    dp = [[inf] * 2 for _ in range(M + 1)]

    for i in range(N):
        a = A[i]
        ndp = [[inf] * 2 for _ in range(M + 1)]
        ndp[0][0] = 1
        for j in range(1, M + 1):
            if i == 0:
                if j == a:
                    ndp[a][1] = 0
            else:
                ndp[j][0] = min(dp[j][1] + 1, dp[j][0])
                if j >= A[i]:
                    ndp[j][1] = min(dp[j - a][0], dp[j - a][1])
        dp = ndp

    for j in range(1, M + 1):
        ans = min(dp[j])
        print(-1 if ans >= inf else ans)


def solve_ac1(N: int, M: int, A: "List[int]"):
    inf = 10**9
    # dp: List[List[List[int]]] = [[[inf] * 2 for _ in range(M + 1)] for _ in range(N)]
    dp = [inf] * (N * (M + 1) * 2)

    def _idx(_i, _j, _k):
        return _i*2*(M+1) + _j*2 + _k

    for i in range(N):
        a = A[i]
        # print(_idx(i, 0, 0), N, M + 1, (N * (M + 1) * 2), i)
        dp[_idx(i, 0, 0)] = 1
        # dp[i][0][0] = 1
        for j in range(1, M + 1):
            if i == 0:
                if j == a:
                    dp[_idx(0, a, 1)] = 0
                    # dp[0][a][1] = 0
            else:
                # dp[i][j][0] = min(dp[i - 1][j][1] + 1, dp[i - 1][j][0])
                dp[_idx(i, j, 0)] = min(dp[_idx(i - 1, j, 1)] + 1, dp[_idx(i - 1, j, 0)])
                if j >= A[i]:
                    # dp[i][j][1] = min(dp[i - 1][j - a][0], dp[i - 1][j - a][1])
                    dp[_idx(i, j, 1)] = min(dp[_idx(i - 1, j - a, 0)], dp[_idx(i - 1, j - a, 1)])

    for j in range(1, M + 1):
        # ans = min(dp[N - 1][j])
        ans = min(dp[_idx(N - 1, j, 0)], dp[_idx(N - 1, j, 1)])
        print(-1 if ans >= inf else ans)


def solve_tle(N: int, M: int, A: "List[int]"):
    """
    3次元のリストの初期化だけで1700ms使ってしまい、TLE。簡単な対策は2つ
    - 実は2次元でよい。なぜなら過去のステートは「直前」以外使用しないから
    - 3次元のリストではなく1次元(2次元)にリストを潰す。初期化が150ms〜300msくらいになるので十分間に合うようになる
    """
    inf = 10**9
    dp: List[List[List[int]]] = [[[inf] * 2 for _ in range(M + 1)] for _ in range(N)]

    for i in range(N):
        a = A[i]
        dp[i][0][0] = 1
        for j in range(1, M + 1):
            if i == 0:
                if j == a:
                    dp[0][a][1] = 0
            else:
                dp[i][j][0] = min(dp[i - 1][j][1] + 1, dp[i - 1][j][0])
                if j >= A[i]:
                    dp[i][j][1] = min(dp[i - 1][j - a][0], dp[i - 1][j - a][1])

    for j in range(1, M + 1):
        ans = min(dp[N - 1][j])
        print(-1 if ans >= inf else ans)



def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, a)


if __name__ == "__main__":
    main()
