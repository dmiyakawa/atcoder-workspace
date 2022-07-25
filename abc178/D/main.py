#!/usr/bin/env python3

MOD = 1000000007


def solve_ref(S: int):
    dp = [0 for _ in range(max(S + 1, 20))]
    dp[3] = 1
    for n in range(4, S + 1):
        dp[n] = (dp[n - 1] + dp[n - 3]) % MOD
    return dp[S]


def solve_wa(S: int):
    S_d = S // 3
    # 長さi[0, S_d]の数列で、各要素が0以上かつ合計j ([0, S])となるの個数
    dp = [[0 for _ in range(S + 2)] for _ in range(S_d + 2)]
    for j in range(S + 1):
        dp[1][j] = 1
    for i in range(S_d + 1):
        dp[i][1] = i
    for i in range(2, S_d + 1):
        for j in range(2, S + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    ans = 0
    for i in range(1, S_d + 1):
        # 長さi列の数列で各要素は必ず3以上なので、割り振れるのはそれを引いた数
        rem = S - i * 3
        ans += dp[i][rem]

    return ans % MOD


def main():
    S = int(input())
    print(solve_ref(S))


if __name__ == "__main__":
    main()
