#!/usr/bin/env python3

from collections import deque


def main():
    R, C = map(int, input().split())
    sy, sx = [int(e) - 1 for e in input().split()]
    gy, gx = [int(e) - 1 for e in input().split()]
    grid = [list(input()) for _ in range(R)]
    to_visit = deque([(sx, sy, 0)])
    visited = set()
    while to_visit:
        x, y, cost = to_visit.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        to_check = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        for x0, y0 in to_check:
            if (x0, y0) == (gx, gy):
                print(cost + 1)
                return
            if x0 < 0 or C <= x0 or y0 < 0 or R <= y0 or grid[y0][x0] == "#":
                continue
            to_visit.append((x0, y0, cost + 1))

    return -1


if __name__ == "__main__":
    main()
