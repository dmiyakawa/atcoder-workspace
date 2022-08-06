#!/usr/bin/env python3


MOD = 998244353  # type: int


def solve_ref(N: int, K: int, P: "List[int]", Q: "List[int]"):
    """https://atcoder.jp/contests/abc238/editorial/3354"""
    dp = [[[0 for _ in range(N + 2)] for _ in range(K + 1)] for _ in range(N + 1)]
    Qs = [q for _, q in sorted((p, q) for p, q in zip(P, Q))]
    # print(Qs)
    # p人目は1つ目の科目でp位、2つ目の科目でq位
    for p, q in enumerate(Qs, start=1):
        if p == 1:
            # 一人目を選ばなかった
            dp[1][0][q] = 1
            # 一人目を選んだ
            dp[1][1][N + 1] = 1
        else:
            # p - 1人目までの間にk人選んでいる
            for k in range(max(0, p - 1 - N + K), min(p - 1, K) + 1):
                # K人までしか選ぶ選択はできない
                if k < K:
                    # p人目を選んだ場合、その人の2科目目の順位であるq位より良い順位の人を先に選ばなかったという状態にはできない
                    for j in range(q, N + 2):
                        dp[p][k + 1][j] = dp[p - 1][k][j]
                # p人目を選ばなかった場合、選ばなかった人物のうち、最も小さい順位は最大でもq位になる
                if k > p - 1 - N + K:
                    for j in range(q):
                        # すでにq位未満の人が選ばれていない場合、選ばなかった人物のうち、最も小さい順位は変動しない
                        dp[p][k][j] = (dp[p][k][j] + dp[p - 1][k][j]) % MOD
                    dp[p][k][q] = (dp[p][k][q] + sum(dp[p - 1][k][q + 1:])) % MOD
        # print(p, dp[p])
    print(sum(dp[N][K]) % MOD)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_ref(N, K, P, Q)




if __name__ == "__main__":
    main()
