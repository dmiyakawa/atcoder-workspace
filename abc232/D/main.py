#!/usr/bin/env python3


def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[H - 1][W - 1] = 1 if C[H - 1][W - 1] == "." else 0
    for i in range(H - 2, -1, -1):
        dp[i][W - 1] = dp[i + 1][W - 1] + 1 if C[i][W - 1] == "." else 0
    for j in range(W - 2, -1, -1):
        dp[H - 1][j] = dp[H - 1][j + 1] + 1 if C[H - 1][j] == "." else 0
    for i in range(H - 2, -1, -1):
        for j in range(W - 2, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]) + 1 if C[i][j] == "." else 0
    print(dp[0][0])


if __name__ == "__main__":
    main()
