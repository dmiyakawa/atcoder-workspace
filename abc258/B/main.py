#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]"):
    max_num = 0
    for x in range(0, N):
        for y in range(0, N):
            for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                rx, ry = x, y
                lst = []
                for _ in range(N):
                    lst.append(A[rx][ry])
                    rx = (rx + dx) % N
                    ry = (ry + dy) % N
                max_num = max(max_num, int("".join(str(n) for n in lst)))
    print(max_num)


def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(input())
    solve(N, A)


if __name__ == "__main__":
    main()
