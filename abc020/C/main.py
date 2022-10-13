#!/usr/bin/env python3

import sys
from collections import deque

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    H, W, T = map(int, input().split())
    S = [input().strip() for _ in range(H)]
    start = -1
    goal = -1
    for i, line in enumerate(S):
        for j, ch in enumerate(line):
            if ch == "S":
                start = i*W+j
            elif ch == "G":
                goal = i*W+j
    to_visit = deque([start])
    cost = [-1] * (H*W)
    # 0-1 BFSでは解けないねこれ
    while to_visit:
        u, c = to_visit.pop()
        if 0 <= cost[u] <= c:
            continue
        cost[u] = c
        if u == goal:
            break
        for h, w in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            vh, vw = u[0] + h, u[1] + w
            v = vh*W + vw
            if not (0 <= v[0] < H and 0 <= v[1] < W and cost[v] < 0):
                continue
            if S[vh][vw] == "#":
                to_visit.appendleft((v, c + 1))
            else:
                to_visit.append((v, c))
    cost[goal]


if __name__ == "__main__":
    main()
