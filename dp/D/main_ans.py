#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    items = list(zip(w, v))
    dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]
    dp[0][0] = 0

    # i + 1 個 (<= N)まで選べるとする
    for i in range(N):
        dp[i + 1] = dp[i].copy()

        # j (< W) の重さ分まですでに入っているとしたとき
        for j in range(W):
            if dp[i][j] != -1:
                # i + 1 個めを入れても W を超えない場合
                if j + items[i][0] <= W:
                    # i + 1 個めを入れた場合の方が価値が大きくなるようなら、そちらを選択する
                    dp[i + 1][j + items[i][0]] = max(dp[i][j] + items[i][1], dp[i + 1][j + items[i][0]])

    print(max(dp[N]))


if __name__ == "__main__":
    main()
