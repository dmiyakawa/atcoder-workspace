#!/usr/bin/env python3

from typing import List

MOD = 998244353  # type: int


def solve(T: int, N: "List[int]", S: "List[str]"):
    """\
    RE + TLE版を手直ししたもの https://atcoder.jp/contests/abc242/submissions/35082792
    スライスで部分文字列が生成される部分が致命的に遅かったので、左端と右端を変数に持つようにした
    スライスの計算量は実際kを部分文字列の長さとした時 O(k) なので、O(N^2)と同じ問題を抱える
    https://wiki.python.org/moin/TimeComplexity
    """
    M = max(N)
    dp = [0] * (M + 1)
    dp[1] = 26
    if M >= 2:
        dp[2] = 26
    for i in range(3, M + 1):
        dp[i] = dp[i - 2] * 26
        dp[i] %= MOD

    for n, s in zip(N, S):
        ans = dp[n]
        tmp = []
        left, right = 0, len(s) - 1
        # 参考: スライスを使った場合TLEになる例 https://atcoder.jp/contests/abc242/submissions/35083099
        # while s:
        while left <= right:
            len_s = right - left + 1
            head, tail = ord(s[left]) - ord("A"), ord(s[right]) - ord("A")
            # len_s = len(s)
            # head, tail = ord(s[0]) - ord("A"), ord(s[-1]) - ord("A")
            tmp.append((head, tail))
            ans -= (25 - head) * (dp[len_s - 2] if len_s > 2 else 1)
            ans %= MOD
            left += 1
            right -= 1
            # s = s[1:-1]

        incl_eq = True
        while tmp:
            head, tail = tmp.pop()
            if head < tail:
                break
            elif head > tail:
                incl_eq = False
                break
        if not incl_eq:
            ans -= 1
        print(ans % MOD)


def solve_1(T: int, N: "List[int]", S: "List[str]"):
    """初AC https://atcoder.jp/contests/abc242/submissions/35082792"""
    M = max(N)
    dp = [0] * (M + 1)
    dp[1] = 26
    if M >= 2:
        dp[2] = 26
    for i in range(3, M + 1):
        dp[i] = dp[i - 2] * 26
        dp[i] %= MOD
    for n, s in zip(N, S):
        ans = dp[n]
        lst = [ord(ch) - ord("A") for ch in s]
        left, right = 0, len(s) - 1
        while left <= right:
            head, tail = lst[left], lst[right]
            lst_len = right - left + 1
            if lst_len > 2:
                ans -= (25 - head) * dp[lst_len - 2]
            else:
                ans -= 25 - head
            ans %= MOD
            left += 1
            right -= 1

        left -= 1
        right += 1
        incl_eq = True
        while left >= 0:
            head, tail = lst[left], lst[right]
            if head < tail:
                break
            elif head > tail:
                incl_eq = False
                break
            left -= 1
            right += 1
        if not incl_eq:
            ans -= 1
        print(ans % MOD)


def solve_re_tle(T: int, N: "List[int]", S: "List[str]"):
    """\
    https://atcoder.jp/contests/abc242/submissions/35082585
    REはT=1, N=1のケースなどで自明に発生する
    """
    M = max(N)
    dp = [0] * (M + 1)
    dp[1], dp[2] = 26, 26
    for i in range(3, M + 1):
        dp[i] = dp[i - 2] * 26
        dp[i] %= MOD
    for n, s in zip(N, S):
        ans = dp[n]
        tmp = []
        while s:
            head, tail = ord(s[0]) - ord("A"), ord(s[-1]) - ord("A")
            tmp.append((head, tail))
            ans -= (25 - head) * (dp[len(s) - 2] if len(s) > 2 else 1)
            ans %= MOD
            # この文字列操作が致命的に遅い
            s = s[1:-1]

        incl_eq = True
        while tmp:
            head, tail = tmp.pop()
            if head < tail:
                break
            elif head > tail:
                incl_eq = False
                break
        if not incl_eq:
            ans -= 1
        print(ans % MOD)


def main():
    import sys
    sys.setrecursionlimit(2 * (10 ** 5))

    input = sys.stdin.readline
    T = int(input())
    N = [0] * T
    S = [""] * T
    for i in range(T):
        N[i] = int(input())
        S[i] = input().rstrip()
    solve(T, N, S)


def main():
    import sys
    sys.setrecursionlimit(2 * (10 ** 5))

    input = sys.stdin.readline
    T = int(input())
    N = [0] * T
    S = [""] * T
    for i in range(T):
        N[i] = int(input())
        S[i] = input().rstrip()
    solve(T, N, S)


if __name__ == "__main__":
    main()
