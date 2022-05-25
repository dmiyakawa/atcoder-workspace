#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))


def main():
    H, W = [int(e) for e in input().split()]
    C = [list(input()) for _ in range(H)]
    max_path_length = -1
    for h, lst in enumerate(C):
        for w, cell in enumerate(lst):
            if cell == ".":
                max_path_length = max(find_path(H, W, C, h, w, h, w, {(h, w)}), max_path_length)
    print(max_path_length)


def find_path(H, W, C, sh, sw, ch, cw, visited) -> int:
    path_length = -1
    for h, w in [(ch - 1, cw), (ch + 1, cw), (ch, cw - 1), (ch, cw + 1)]:
        if (h, w) == (sh, sw) and len(visited) > 2:
            path_length = max(path_length, len(visited))
        elif 0 <= h < H and 0 <= w < W and C[h][w] == "." and (h, w) not in visited:
            path_length = max(path_length, find_path(H, W, C, sh, sw, h, w, visited | {(h, w)}))
    return path_length


if __name__ == "__main__":
    main()
