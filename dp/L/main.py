#!/usr/bin/env python3

from typing import List, Optional


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    # solve_tle(N, A)
    # solve_memo(N, A)
    solve_plain_dp(N, A)


def solve_plain_dp(N, A):
    # 他のAC例が多い実装。区間DP
    # N <= 3000 より O(N^2) で間に合う
    # 400ms程度
    # https://atcoder.jp/contests/dp/submissions/33343348
    dp: List[List[Optional[int]]] = [[None for _ in range(N)] for _ in range(N)]
    for l in range(N - 1, -1, -1):
        for r in range(l, N):
            if l == r:
                dp[l][r] = A[l]
            else:
                dp[l][r] = max((A[l] - dp[l + 1][r]) if l < N - 1 else 0,
                               (A[r] - dp[l][r - 1]) if r > 0 else 0)
    print(dp[0][N - 1])


def solve_memo(N, A):
    # メモ化再帰を関数のスタックを使わずに実装したバージョン
    # 1300ms程度。区間DPで愚直にやるよりも遅め
    # https://atcoder.jp/contests/dp/submissions/33343379
    dp: List[List[Optional[int]]] = [[None for _ in range(N)] for _ in range(N)]
    stack = [(0, N - 1)]
    while stack:
        l, r = stack[-1]
        if dp[l][r] is not None:
            stack.pop()
            continue
        if l == r:
            dp[l][r] = A[l]
            stack.pop()
            continue
        recurse = False
        if dp[l + 1][r] is None:
            stack.append((l + 1, r))
            recurse = True
        if dp[l][r - 1] is None:
            stack.append((l, r - 1))
            recurse = True
        if recurse:
            continue
        dp[l][r] = max(A[l] - dp[l + 1][r], A[r] - dp[l][r - 1])
        stack.pop()

    print(dp[0][N - 1])


def solve_tle(N, A):
    from functools import lru_cache
    import sys
    # 公式解説の通り（メモ化再帰）だがPythonだとPyPyでもTLEする。たぶん、PyPyが再帰に弱いため
    sys.setrecursionlimit(2 * (10 ** 5))

    # これをやってもダメ
    import pypyjit
    pypyjit.set_param("max_unroll_recursion=-1")

    @lru_cache(None)
    def _solve(l, r):
        if l == r:
            return A[l]
        return max(A[l] - _solve(l + 1, r), A[r] - _solve(l, r - 1))

    print(_solve(0, N - 1))


if __name__ == "__main__":
    main()
