#!/usr/bin/env python3
#
# 解説読了後
#

MOD = 998244353  # type: int


def main():
    N, M, K = map(int, input().split())
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for m in range(1, M + 1):
        dp[0][m] = 1

    for n in range(N - 1):
        for k in range(1, K + 1):
            for m in range(1, M + 1):
                if k + m > K:
                    break
                dp[n + 1][k + m] = (dp[n + 1][k + m] + dp[n][k]) % MOD
    print(sum(dp[N - 1][k] for k in range(1, K + 1)) % MOD)


if __name__ == "__main__":
    main()
