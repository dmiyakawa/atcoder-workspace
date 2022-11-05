#!/usr/bin/env python3


def main():
    import sys
    input = sys.stdin.readline
    W = int(input())
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 幅w消費済、k枚使用済のときの最大価値
    dp = [[0] * (K + 1) for _ in range(W + 1)]
    for n, (a, b) in enumerate(zip(A, B)):
        ndp = [[0] * (K + 1) for _ in range(W + 1)]
        for w in range(W + 1):
            for k in range(K + 1):
                prev_1 = 0 if (w - a < 0 or k - 1 < 0) else dp[w - a][k - 1] + b
                prev_2 = 0 if n == 0 else dp[w][k]
                ndp[w][k] = max(dp[w][k], prev_1, prev_2)
        dp = ndp

    # print(dp)
    print(dp[W][K])


if __name__ == "__main__":
    main()
