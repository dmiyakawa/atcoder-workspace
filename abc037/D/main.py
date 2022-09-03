#!/usr/bin/env python3

MOD = 1000000007  # type: int


def main_2():
    """タプル不使用版 https://atcoder.jp/contests/abc037/submissions/34519174
    667ms
    """
    import sys
    H, W = map(int, sys.stdin.buffer.readline().split())
    N = H * W
    A = list(map(int, sys.stdin.buffer.read().split()))
    offset = 10**6
    B = [A[i] * offset + i for i in range(N)]
    B.sort(reverse=True)
    dp = [0] * N
    count = 0
    for b in B:
        a, i = b // offset, b % offset
        h, w = i // W, i % W
        if h - 1 >= 0 and A[i - W] > a:
            dp[i] += dp[i - W]
            dp[i] %= MOD
        if h + 1 < H and A[i + W] > a:
            dp[i] += dp[i + W]
            dp[i] %= MOD
        if w - 1 >= 0 and A[i - 1] > a:
            dp[i] += dp[i - 1]
            dp[i] %= MOD
        if w + 1 < W and A[i + 1] > a:
            dp[i] += dp[i + 1]
            dp[i] %= MOD
        dp[i] += 1
        count += dp[i]
        count %= MOD

    print(count)


def main():
    """初AC版 https://atcoder.jp/contests/abc037/submissions/34518975
    衝撃の1999ms"""
    import sys
    H, W = map(int, sys.stdin.buffer.readline().split())
    N = H * W
    A = list(map(int, sys.stdin.buffer.read().split()))
    B = [(A[i], i) for i in range(N)]
    B.sort(reverse=True, key=lambda b: b[0])
    dp = [0] * N
    count = 0
    for (a, i) in B:
        h, w = i // W, i % W
        if h - 1 >= 0 and A[i - W] > a:
            dp[i] += dp[i - W]
            dp[i] %= MOD
        if h + 1 < H and A[i + W] > a:
            dp[i] += dp[i + W]
            dp[i] %= MOD
        if w - 1 >= 0 and A[i - 1] > a:
            dp[i] += dp[i - 1]
            dp[i] %= MOD
        if w + 1 < W and A[i + 1] > a:
            dp[i] += dp[i + 1]
            dp[i] %= MOD
        dp[i] += 1
        count += dp[i]
        count %= MOD

    print(count)


def main_ref():
    """https://atcoder.jp/contests/abc037/submissions/33782248"""
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    starts = []
    mod = 10 ** 9 + 7
    hw = 1000000
    ans = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            starts.append(i + j * 1000 + A[i][j] * hw)
    starts.sort(reverse=True)
    answer = 0
    for num in starts:
        i = num % 1000
        j = num // 1000 % 1000
        ans[i][j] += 1
        if i != 0:
            if A[i][j] != A[i - 1][j]:
                ans[i][j] += ans[i - 1][j]
                ans[i][j] %= mod
        if i != H - 1:
            if A[i][j] != A[i + 1][j]:
                ans[i][j] += ans[i + 1][j]
                ans[i][j] %= mod
        if j != 0:
            if A[i][j] != A[i][j - 1]:
                ans[i][j] += ans[i][j - 1]
                ans[i][j] %= mod
        if j != W - 1:
            if A[i][j] != A[i][j + 1]:
                ans[i][j] += ans[i][j + 1]
                ans[i][j] %= mod
        answer += ans[i][j]
        answer %= mod
    # print(ans)
    print(answer)


if __name__ == "__main__":
    main_2()
