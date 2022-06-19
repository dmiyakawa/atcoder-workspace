#!/usr/bin/env python3

def main():
    # 起点を 0 にしとく
    h1, h2, h3, w1, w2, w3 = [int(e) - 3 for e in input().split()]
    grid = [[0 for _ in range(3)] for _ in range(3)]
    count = 0
    # (0, 0)を設定
    for c00 in range(min(h1, w1) + 1):
        grid[0][0] = c00
        # 0列目を縦
        for c10 in range(w1 - c00 + 1):
            grid[1][0] = c10
            grid[2][0] = w1 - c00 - c10
            # 0行目を横
            for c01 in range(h1 - c00 + 1):
                grid[0][1] = c01
                grid[0][2] = h1 - c00 - c01
                for c11 in range(h2 - c10 + 1):
                    grid[1][1] = c11
                    grid[1][2] = h2 - c10 - c11
                    if w2 - c01 - c11 < 0:
                        continue
                    grid[2][1] = w2 - c01 - c11
                    if (
                            h3 - grid[2][0] - grid[2][1] < 0
                            or w3 - grid[0][2] - grid[1][2] < 0
                            or h3 - grid[2][0] - grid[2][1] != w3 - grid[0][2] - grid[1][2]
                    ):
                        continue
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
