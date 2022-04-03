#!/usr/bin/env python3
#
# 公式解答の 01-BFS
# https://atcoder.jp/contests/abc246/editorial/3702
#
# https://atcoder.jp/contests/abc246/submissions/30699317
#

from collections import deque
from typing import List

Inf = INF = float("INF")

LT, RT, RB, LB = 0, 1, 2, 3


def main():
    N = int(input())
    A_x, A_y = [int(e) - 1 for e in input().split()]
    B_x, B_y = [int(e) - 1 for e in input().split()]
    S: List[str] = [input().rstrip() for _ in range(N)]
    print(solve(N, A_x, A_y, B_x, B_y, S))


def solve(N: int, A_x: int, A_y: int, B_x: int, B_y: int, S: List[str]):
    # 3次元リストでも制限時間がゆるいので間に合うが、2〜3倍遅くなる
    # https://atcoder.jp/contests/abc246/submissions/30698443
    costs: List[float] = [Inf] * N * N * 4

    def _index(_x, _y, _dr) -> int:
        return 4 * N * _x + 4 * _y + _dr

    deq = deque()
    for i in range(4):
        costs[_index(A_x, A_y, i)] = 1
        deq.append((A_x, A_y, i))

    min_cost = Inf
    while deq:
        x, y, dr = deq.popleft()
        cost = costs[_index(x, y, dr)]

        for (dx, dy, ddr) in [(-1, 1, LT), (1, 1, RT), (1, -1, RB), (-1, -1, LB)]:
            xx, yy = x + dx, y + dy
            if 0 <= xx < N and 0 <= yy < N and S[xx][yy] != "#":
                new_cost = cost + (0 if dr == ddr else 1)

                if new_cost >= costs[_index(xx, yy, ddr)] or new_cost >= min_cost:
                    continue
                costs[_index(xx, yy, ddr)] = new_cost

                if (xx, yy) == (B_x, B_y):
                    min_cost = min(min_cost, new_cost)
                    break

                if dr == ddr:
                    deq.appendleft((xx, yy, ddr))
                else:
                    deq.append((xx, yy, ddr))

    if min_cost is not Inf:
        return min_cost
    return -1


if __name__ == "__main__":
    main()
