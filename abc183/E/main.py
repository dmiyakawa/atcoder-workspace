#!/usr/bin/env python3

MOD = 1000000007  # type: int


def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    c = [[0] * W for _ in range(H)]
    # vertical, horizontal, skew 各方向に累積和的な考え方を導入する
    acc_ver = [[0] * W for _ in range(H)]
    acc_hor = [[0] * W for _ in range(H)]
    acc_skw = [[0] * W for _ in range(H)]
    c[0][0] = 1
    acc_ver[0][0] = 1
    acc_hor[0][0] = 1
    acc_skw[0][0] = 1
    for i in range(H):
        for j in range(W):
            if grid[i][j] != ".":
                continue
            if i > 0 and j > 0 and grid[i - 1][j - 1] == ".":
                c[i][j] += acc_skw[i - 1][j - 1]
            if i > 0 and grid[i - 1][j] == ".":
                c[i][j] += acc_ver[i - 1][j]
            if j > 0 and grid[i][j - 1] == ".":
                c[i][j] += acc_hor[i][j - 1]
            c[i][j] %= MOD
            acc_ver[i][j] = c[i][j]
            acc_hor[i][j] = c[i][j]
            acc_skw[i][j] = c[i][j]
            if i > 0 and j > 0 and grid[i - 1][j - 1] == ".":
                acc_skw[i][j] += acc_skw[i - 1][j - 1]
                acc_skw[i][j] %= MOD
            if i > 0 and grid[i - 1][j] == ".":
                acc_ver[i][j] += acc_ver[i - 1][j]
                acc_ver[i][j] %= MOD
            if j > 0 and grid[i][j - 1] == ".":
                acc_hor[i][j] += acc_hor[i][j - 1]
                acc_hor[i][j] %= MOD
    # for l in acc_ver:
    #     print(l)
    # print()
    # for l in acc_hor:
    #     print(l)
    # print()
    # for l in acc_skw:
    #     print(l)
    # print()
    # for l in c:
    #     print(l)
    print(c[H - 1][W - 1] % MOD)


if __name__ == "__main__":
    main()
