#!/usr/bin/env python3
from collections import deque


def main_2():
    """\
    BFS。まぁこっちだろうなぁ
    """
    H, W = map(int, input().split())
    S = [list(input().rstrip()) for _ in range(H)]

    max_cost = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            visited = set()
            to_visit = deque([(i, j, 0)])
            while to_visit:
                h, w, c = to_visit.pop()
                if (h, w) in visited:
                    continue
                visited.add((h, w))
                max_cost = max(c, max_cost)
                for vh, vw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    h0, w0 = h + vh, w + vw
                    if 0 <= h0 < H and 0 <= w0 < W and S[h0][w0] == "." and (h0, w0) not in visited:
                        to_visit.appendleft((h0, w0, c + 1))
    print(max_cost)


def main():
    """\
    初AC。ワーシャルフロイド
    問題内容に比して準備が無意味に煩雑でタイプ数も多いので、解けてはいるけどいまいち感ある
    """
    Inf = float("inf")

    H, W = map(int, input().split())
    S = [list(input().rstrip()) for _ in range(H)]
    grid = [[-1] * W for _ in range(H)]
    C = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                grid[i][j] = C
                C += 1

    d = [[Inf] * C for _ in range(C)]
    for i in range(H):
        for j in range(W):
            u = grid[i][j]
            if u >= 0:
                d[u][u] = 0
                if i > 0 and grid[i - 1][j] >= 0:
                    v = grid[i - 1][j]
                    d[u][v] = d[v][u] = 1
                if j > 0 and grid[i][j - 1] >= 0:
                    v = grid[i][j - 1]
                    d[u][v] = d[v][u] = 1

    for k in range(C):
        for i in range(C):
            for j in range(C):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    ans = 0
    for i in range(C):
        ans = max(ans, max(v for v in d[i] if v != Inf))
    print(ans)


if __name__ == "__main__":
    main_2()
