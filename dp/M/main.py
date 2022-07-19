#!/usr/bin/env python3

MOD = 1000000007


def main2():
    # 解説に基づいた想定解法。累積和を取る
    N, K = map(int, input().split())
    A = [int(e) for e in input().split()]
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        cum = []
        for j in range(K + 1):
            cum.append(dp[i - 1][j] + (cum[j - 1] if j > 0 else 0))
        for j in range(K + 1):
            dp[i][j] = (cum[j] - (cum[j - A[i - 1] - 1] if j - A[i - 1] > 0 else 0)) % MOD

            # for k in range(A[i - 1] + 1):
            #     if j - k >= 0:
            #         dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    print(dp[N][K] % MOD)


def main():
    # ACしているが、想定解法とは（やっていることは本質的に同じながら）やや考え方が異なる
    #
    # それぞれの子供に配れる飴の個数を超すと超す前なら加算できた組み合わせが行えなくなる
    # 例として以下の入力を考える
    # > 3 4
    # > 3 2 1
    #
    # 縦をK、横を子供1, 2, 3として表を構築すると
    #
    # (0) 1 1 1
    # (1) 1 2 3
    # (2) 1 3 !
    # (3) 1 ! !
    # (4) 0 ! ?
    #
    # 求めたいのは?で、上記で数値が含まれている部分は飴の個数に制限がない組み合わせ
    # !の箇所では飴を配る組み合わせが制限がない場合と比べて減る。
    # どのくらい減るかと言うと、一つ前のこどもに飴を配らないパターン分
    # 例えば K = 2, N = 3 について "0 0 2" という組み合わせは選べなくなる -> 3 + 3 - 1 = 5
    # K = 3, N = 3 について "0 0 3" に加えて "1 0 2", "0 1 2" という組み合わせは選べなくなる -> 3 + 5 - 2 = 6
    # K = 4, N = 3 について、上の３つの組み合わせに加えてさらに３通りの組み合わせが選べなくなる -> 2 + 6 - 3 = 5
    N, K = map(int, input().split())
    A = [int(e) for e in input().split()]
    dp = [[0 for _ in range(K + 1)] for _ in range(N)]
    for i in range(N):
        dp[i][0] = 1
    for i in range(1, A[0] + 1):
        dp[0][i] = 1

    for i in range(1, N):
        for k in range(1, K + 1):
            dp[i][k] = (dp[i - 1][k] + dp[i][k - 1] - (dp[i - 1][k - A[i] - 1] if k - A[i] > 0 else 0)) % MOD

    print(dp[N - 1][K] % MOD)


if __name__ == "__main__":
    main2()
