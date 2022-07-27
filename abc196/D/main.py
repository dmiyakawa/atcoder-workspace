#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))


def count(H, W, A, B, rows):
    if A == 0 and B == 0:
        return 1
    N = H * W

    ret = 0
    for i in range(N):
        if rows[i] == 1:
            continue
        h, w = divmod(i, W)
        if A > 0:
            if w + 1 < W and rows[i + 1] == 0:
                ret += count(H, W, A - 1, B, [1 if j in [i, i + 1] else rows[j] for j in range(N)])
            if h + 1 < H and rows[i + W] == 0:
                ret += count(H, W, A - 1, B, [1 if j in [i, i + W] else rows[j] for j in range(N)])
        if B > 0:
            ret += count(H, W, A, B - 1, [1 if j == i else rows[j] for j in range(N)])
        break
    return ret


def solve(H: int, W: int, A: int, B: int):
    print(count(H, W, A, B, [0 for _ in range(H * W)]))


def main():
    solve(*map(int, input().split()))


if __name__ == "__main__":
    main()
