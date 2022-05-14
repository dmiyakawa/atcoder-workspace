#!/usr/bin/env python3


def main():
    N = int(input())
    squares = [tuple(int(e) for e in input().split()) for _ in range(N)]
    d_bottom = {}
    d_top = {}

    for i, (lx, ly, ry, ry) in enumerate(squares):
        d_bottom.setdefault(ly, set()).add(i)
        d_top.setdefault(ry, set()).add(i)

    lefts = {}
    rights = {}
    counts = {}
    for y in range(0, 1000):
        for i in d_bottom.get(y, set()):
            lx, ly, rx, ry = squares[i]
            lefts[lx] = lefts.get(lx, 0) + 1
            rights[rx] = rights.get(rx, 0) + 1

        for i in d_top.get(y, set()):
            lx, ly, rx, ry = squares[i]
            lefts[lx] -= 1
            rights[rx] -= 1

        current_k = 0
        for x in range(0, 1000):
            current_k = current_k + lefts.get(x, 0) - rights.get(x, 0)
            counts[current_k] = counts.get(current_k, 0) + 1
    for k in range(1, N + 1):
        print(counts.get(k, 0))


def main_imos():
    # https://atcoder.jp/contests/typical90/submissions/31604408
    H_W_LEN = 10 ** 3 + 1
    N = int(input())
    lx, ly, rx, ry = [], [], [], []
    for _ in range(N):
        a, b, c, d = [int(e) for e in input().split()]
        lx.append(a)
        ly.append(b)
        rx.append(c)
        ry.append(d)

    table = [[0 for _ in range(H_W_LEN)] for _ in range(H_W_LEN)]
    for i in range(N):
        table[lx[i]][ly[i]] += 1
        table[rx[i]][ry[i]] += 1
        table[lx[i]][ry[i]] -= 1
        table[rx[i]][ly[i]] -= 1
    for x in range(H_W_LEN):
        y_sum = 0
        for y in range(H_W_LEN):
            y_sum += table[x][y]
            table[x][y] = y_sum
    for y in range(H_W_LEN):
        x_sum = 0
        for x in range(H_W_LEN):
            x_sum += table[x][y]
            table[x][y] = x_sum
    ans = [0 for _ in range(N)]
    for i in range(H_W_LEN):
        for j in range(H_W_LEN):
            if table[i][j] > 0:
                ans[table[i][j] - 1] += 1
    for i in ans:
        print(i)


if __name__ == "__main__":
    main_imos()
    # main()

