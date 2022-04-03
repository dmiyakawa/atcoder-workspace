#!/usr/bin/env python3

import heapq
import sys
from typing import List, Union

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():
    N = int(input())
    A_x, A_y = [int(e) for e in input().split()]
    B_x, B_y = [int(e) for e in input().split()]
    S: List[str] = [input().rstrip() for _ in range(N)]
    print(solve(N, A_x, A_y, B_x, B_y, S))


def solve(N: int, A_x: int, A_y: int, B_x: int, B_y: int, S: List[str]):
    A_x -= 1
    A_y -= 1
    B_x -= 1
    B_y -= 1
    visited_costs: List[List[int]] = [[0] * N for _ in range(N)]
    spanned = [[False] * N for _ in range(N)]
    hq = [(0, A_x, A_y)]
    while hq:
        cost, x, y = heapq.heappop(hq)
        if spanned[x][y]:
            continue
        spanned[x][y] = True

        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            xx, yy = x + dx, y + dy
            while 0 <= xx < N and 0 <= yy < N:
                if S[xx][yy] == "#":
                    break
                if visited_costs[xx][yy] > 0:
                    xx += dx
                    yy += dy
                    continue
                visited_costs[xx][yy] = cost + 1
                if (xx, yy) == (B_x, B_y):
                    return cost + 1
                heapq.heappush(hq, (cost + 1, xx, yy))
                xx += dx
                yy += dy

    return -1


if __name__ == "__main__":
    main()
