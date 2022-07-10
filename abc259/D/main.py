#!/usr/bin/env python3

import math
from collections import defaultdict


def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    Cs = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        Cs.append((x, y, r))

    links = defaultdict(set)
    starts = set()
    goals = set()

    for i in range(N):
        x0, y0, r0 = Cs[i]
        if (x0 - s_x) ** 2 + (y0 - s_y) ** 2 == r0 ** 2:
            starts.add(i)
        if (x0 - t_x) ** 2 + (y0 - t_y) ** 2 == r0 ** 2:
            goals.add(i)

        for j in range(i + 1, N):
            x1, y1, r1 = Cs[j]
            d2 = (x1 - x0) ** 2 + (y1 - y0) ** 2
            if d2 < abs(r1 - r0) ** 2 or (r0 + r1) ** 2 < d2:
                continue
            links[i].add(j)
            links[j].add(i)
    assert starts
    assert goals

    to_visit = starts.copy()
    visited = set()

    while to_visit:
        i = to_visit.pop()
        if i in visited:
            continue
        visited.add(i)
        for j in links[i]:
            if j not in visited:
                to_visit.add(j)
    print("Yes" if (visited & goals) else "No")


if __name__ == "__main__":
    main()
