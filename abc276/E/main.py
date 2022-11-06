#!/usr/bin/env python3

from collections import deque


def main():
    H, W = map(int, input().split())
    grid = []
    sh, sw = -1, -1
    for h in range(H):
        line = input()
        grid.append(line)
        if "S" in line:
            w = line.index("S")
            sh, sw = h, w
    assert 0 <= sh < H
    assert 0 <= sw < W
    starts = []
    if 0 < sh and grid[sh - 1][sw] != "#":
        starts.append((sh - 1, sw))
    if sh < H - 1 and grid[sh + 1][sw] != "#":
        starts.append((sh + 1, sw))
    if 0 < sw and grid[sh][sw - 1] != "#":
        starts.append((sh, sw - 1))
    if sw < W - 1 and grid[sh][sw + 1] != "#":
        starts.append((sh, sw + 1))
    while starts:
        ssh, ssw = starts.pop()
        to_visit = deque()
        visited = {(sh, sw)}
        to_visit.append((ssh, ssw, sh, sw))
        while to_visit:
            (i, j, pi, pj) = to_visit.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for i0, j0 in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if i0 < 0 or H <= i0 or j0 < 0 or W <= j0 or grid[i0][j0] == "#" or (i0, j0) == (pi, pj):
                    continue
                if (i0, j0) == (sh, sw):
                    print("Yes")
                    return
                if (i0, j0) in visited:
                    continue
                to_visit.append((i0, j0, i, j))
    print("No")


if __name__ == "__main__":
    main()
