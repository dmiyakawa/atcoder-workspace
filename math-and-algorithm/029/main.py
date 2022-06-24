#!/usr/bin/env python3


def main():
    N = int(input())
    dp = {0: 1, 1: 1}
    for n in range(2, N + 1):
        dp[n] = dp[n - 1] + dp[n - 2]
    print(dp[N])


if __name__ == "__main__":
    main()
