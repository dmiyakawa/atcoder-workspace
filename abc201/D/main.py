#!/usr/bin/env python3


def main():
    import sys
    input = sys.stdin.readline

    H, W = map(int, input().split())
    V = [[(1 if ch == "+" else -1) for ch in input()] for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            turn_takahashi = (i + j) % 2 == 0
            if (i, j) == (H - 1, W - 1):
                continue
            if turn_takahashi:
                dp[i][j] = -10 ** 9
                if i < H - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + V[i + 1][j])
                if j < W - 1:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + V[i][j + 1])
            else:
                dp[i][j] = 10 ** 9
                if i < H - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] - V[i + 1][j])
                if j < W - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] - V[i][j + 1])
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
