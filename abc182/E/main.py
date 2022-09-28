#!/usr/bin/env python3


def main():
    """初AC。ただ、定数レベルで絶妙に遅くTLEギリギリ (2420 ms)
    https://atcoder.jp/contests/abc182/submissions/35200922
    """
    import sys
    input = sys.stdin.buffer.readline
    H, W, N, M = map(int, input().split())
    grids = [0] * (W * H)
    u, l, d, r, li, bl = 0, 1, 2, 3, 4, 5
    for i in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        grids[a * W + b] |= 1 << li

    for i in range(M):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        grids[c * W + d] |= 1 << bl

    BL = 1 << bl
    U = 1 << u
    L = 1 << l
    D = 1 << d
    R = 1 << r
    ULI = 1 << u | 1 << li
    DLI = 1 << d | 1 << li
    LLI = 1 << l | 1 << li
    RLI = 1 << r | 1 << li

    # AC (2420 ms)
    for i in range(H * W):
        if grids[i] & BL:
            continue
        h, w = divmod(i, W)
        if h > 0:
            up = grids[i - W]
            if up & ULI:
                grids[i] |= U
        if w > 0:
            left = grids[i - 1]
            if left & LLI:
                grids[i] |= L
    for i in range(H * W - 1, -1, -1):
        if grids[i] & BL:
            continue
        h, w = divmod(i, W)
        if h < H - 1:
            ds = grids[i + W]
            if ds & DLI:
                grids[i] |= D
        if w < W - 1:
            right = grids[i + 1]
            if right & RLI:
                grids[i] |= R

    # TLE
    # for i in range(H * W):
    #     h, w = divmod(i, W)
    #     i0 = H * W - 1 - i
    #     if h > 0:
    #         if not (grids[i] & BL):
    #             up = grids[(h - 1) * W + w]
    #             if up & ULI:
    #                 grids[i] |= U
    #         if not (grids[i0] & BL):
    #             ds = grids[i0 + W]
    #             if ds & DLI:
    #                 grids[i0] |= D
    #     if w > 0:
    #         if not (grids[i] & BL):
    #             left = grids[h * W + w - 1]
    #             if left & LLI:
    #                 grids[i] |= L
    #         if not (grids[i0] & BL):
    #             right = grids[i0 + 1]
    #             if right & RLI:
    #                 grids[i0] |= R

    ULDRLI = 1 << u | 1 << l | 1 << d | 1 << r | 1 << li
    print(sum(1 for i in range(H * W) if grids[i] & ULDRLI))


def main_ref():
    """
    1292 ms
    https://atcoder.jp/contests/abc182/submissions/35192788
    """
    import itertools

    H, W, N, M = map(int, input().split())
    L = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
    B = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    G1 = [["." for _ in range(W)] for _ in range(H)]
    G2 = [["." for _ in range(W)] for _ in range(H)]
    for a, b in L:
        G1[a][b] = "L"
        G2[a][b] = "L"

    for c, d in B:
        G1[c][d] = "#"
        G2[c][d] = "#"

    for r, c in L:
        nr: int = r + 1
        while nr < H and G1[nr][c] == ".":
            G1[nr][c] = "o"
            nr += 1
        nr = r - 1
        while 0 <= nr and G1[nr][c] == ".":
            G1[nr][c] = "o"
            nr -= 1

    for r, c in L:
        nc: int = c + 1
        while nc < W and G2[r][nc] == ".":
            G2[r][nc] = "o"
            nc += 1
        nc = c - 1
        while 0 <= nc and G2[r][nc] == ".":
            G2[r][nc] = "o"
            nc -= 1

    answer: int = 0
    for i, j in itertools.product(range(H), range(W)):
        if G1[i][j] in ["o", "L"] or G2[i][j] in ["o", "L"]:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main_ref()
