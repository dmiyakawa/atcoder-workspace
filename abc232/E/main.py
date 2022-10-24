#!/usr/bin/env python3


MOD = 998244353  # type: int


def solve(H: int, W: int, K: int, x: "List[int]", y: "List[int]"):
    # 0 ゴールにいる, 1 ゴールと同じ行にいる, 2 ゴールと同じ列にいる, 3 それ以外
    dp = [[0] * 4 for _ in range(K + 1)]
    sx, sy = x[0], y[0]
    dx, dy = x[1], y[1]

    if (sx, sy) == (dx, dy):
        dp[0][0] = 1
    elif sx == dx:
        dp[0][1] = 1
    elif sy == dy:
        dp[0][2] = 1
    else:
        dp[0][3] = 1

    # print(0, dp[0])
    for i in range(1, K + 1):
        dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
        dp[i][0] %= MOD
        dp[i][1] = dp[i - 1][0] * (W - 1) + dp[i - 1][1] * (W - 2) + dp[i - 1][3]
        dp[i][1] %= MOD
        dp[i][2] = dp[i - 1][0] * (H - 1) + dp[i - 1][2] * (H - 2) + dp[i - 1][3]
        dp[i][2] %= MOD
        dp[i][3] = dp[i - 1][1] * (H - 1) + dp[i - 1][2] * (W - 1) + dp[i - 1][3] * (W - 2 + H - 2)
        dp[i][3] %= MOD
        # print(i, dp[i])
    print(dp[K][0] % MOD)


def main():
    import sys

    input = sys.stdin.readline

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (2)  # type: "List[int]"
    y = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(H, W, K, x, y)


if __name__ == "__main__":
    main()
