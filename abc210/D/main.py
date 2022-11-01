#!/usr/bin/env python3


def solve(H: int, W: int, C: int, A: "List[List[int]]"):
    """解説と本質的には同じ。dpの解釈が微妙に違う
    dp_l[i][j] ... 左上から右下に移動する際、一つ駅を建てて一つ以上線路を引いた状態で(i, j)にいるときの最小コスト
    dp_r[i][j] ... 右上から左下に移動する際、一つ駅を建てて一つ以上線路を引いた状態で(i, j)にいるときの最小コスト
    上のdpの場合、各(i, j)においてdp_l[i][j] + A[i][j] と dp_r[i][j] + A[i][j] は線路と駅ふたつを建てた最小コストとなる
    上記のdpを左上、右上のセルから順に実行すると、各セルでの最小コストの最小を得ることができる。これが回答
    """
    inf = float("inf")
    ans = inf
    dp_l = [[inf] * W for _ in range(H)]
    dp_r = [[inf] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            cand_l = inf
            cand_r = inf
            if i > 0:
                cand_l = min(cand_l, dp_l[i - 1][j] + C, A[i - 1][j] + C)
                cand_r = min(cand_r, dp_r[i - 1][W - j - 1] + C, A[i - 1][W - j - 1] + C)
            if j > 0:
                cand_l = min(cand_l, dp_l[i][j - 1] + C, A[i][j - 1] + C)
                cand_r = min(cand_r, dp_r[i][W - j] + C, A[i][W - j] + C)
            dp_l[i][j] = cand_l
            dp_r[i][W - j - 1] = cand_r
            ans = min(ans, cand_l + A[i][j], cand_r + A[i][W - j - 1])
    # print(dp_l)
    # print(dp_r)
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, C, A)


if __name__ == "__main__":
    main()
