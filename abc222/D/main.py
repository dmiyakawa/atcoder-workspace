#!/usr/bin/env python3

MOD = 998244353

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    max_B = max(B)
    dp = [[0 for _ in range(max_B + 1)] for _ in range(N)]
    for c in range(max_B + 1):
        if A[0] <= c <= B[0]:
            dp[0][c] = 1

    for i in range(1, N):
        prev_cum = dp[i - 1].copy()
        for j in range(1, max_B + 1):
            prev_cum[j] = (prev_cum[j] + prev_cum[j - 1]) % MOD

        for c in range(A[i], B[i] + 1):
            dp[i][c] = (prev_cum[c] - (prev_cum[A[i - 1] - 1] if A[i - 1] > 0 else 0)) % MOD
    print(sum(dp[N - 1]) % MOD)


def main_ans():
    # https://atcoder.jp/contests/abc222/editorial/2747
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = 3000
    dp = [1] * (M + 1)
    for i in range(N):
        dp = [(dp[j] if A[i] <= j <= B[i] else 0) for j in range(M + 1)]
        for j in range(M):
            dp[j + 1] += dp[j]
            dp[j + 1] %= MOD
    print(dp[M])


if __name__ == "__main__":
    main_ans()
