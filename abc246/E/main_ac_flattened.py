#!/usr/bin/env python3

from collections import deque
from typing import List, Any

Inf = INF = float("INF")

#
# True
#  - https://atcoder.jp/contests/abc246/submissions/30698395
#  - test_45.txt 2120 ms, test_53.txt 2110 ms
#
# False
#  -
#  - https://atcoder.jp/contests/abc246/submissions/30698443
#  - test_45.txt 4895 ms, test_53.txt 4803 ms
#
#
USE_FLATTENED_LIST = False


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
    LT, RT, RB, LB = 0, 1, 2, 3

    costs: List[Any]
    if USE_FLATTENED_LIST:
        costs: List[float] = [Inf] * N * N * 4

        def _index(_x, _y, _dr) -> int:
            return 4 * N * _x + 4 * _y + _dr
    else:
        costs: List[List[List[float]]] = []
        for _ in range(N):
            tmp1: List[List[float]] = []
            costs.append(tmp1)
            for _ in range(N):
                tmp2: List[float] = [Inf] * 4
                tmp1.append(tmp2)

    deq = deque()
    for i in range(4):
        if USE_FLATTENED_LIST:
            costs[_index(A_x, A_y, i)] = 1
        else:
            costs[A_x][A_y][i] = 1
        deq.append((A_x, A_y, i))

    min_cost = Inf
    while deq:
        x, y, dr = deq.popleft()
        if USE_FLATTENED_LIST:
            cost = costs[_index(x, y, dr)]
        else:
            cost = costs[x][y][dr]

        for (dx, dy, ddr) in [(-1, 1, LT), (1, 1, RT), (1, -1, RB), (-1, -1, LB)]:
            xx, yy = x + dx, y + dy
            if 0 <= xx < N and 0 <= yy < N and S[xx][yy] != "#":
                new_cost = cost + (0 if dr == ddr else 1)

                if USE_FLATTENED_LIST:
                    if new_cost >= costs[_index(xx, yy, ddr)] or new_cost >= min_cost:
                        continue
                    costs[_index(xx, yy, ddr)] = new_cost
                else:
                    if new_cost >= costs[xx][yy][ddr] or new_cost >= min_cost:
                        continue
                    costs[xx][yy][ddr] = new_cost

                if (xx, yy) == (B_x, B_y):
                    min_cost = min(min_cost, new_cost)

                if dr == ddr:
                    deq.appendleft((xx, yy, ddr))
                else:
                    deq.append((xx, yy, ddr))

    if min_cost is not Inf:
        return min_cost
    return -1


if __name__ == "__main__":
    main()
