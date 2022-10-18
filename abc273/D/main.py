#!/usr/bin/env python3
from bisect import bisect_left, bisect_right
from collections import defaultdict


def main():
    import sys
    input = sys.stdin.readline
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    R = [0] * N
    C = [0] * N
    rows_d = defaultdict(list)
    cols_d = defaultdict(list)
    for i in range(N):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        R[i], C[i] = r, c
        rows_d[r].append(c)
        cols_d[c].append(r)
    for r in rows_d:
        rows_d[r].sort()
    for c in cols_d:
        cols_d[c].sort()
    Q = int(input())
    D = [0] * Q
    L = [0] * Q

    r, c = rs - 1, cs - 1
    for i in range(Q):
        d, l = input().split()
        l = int(l)
        D[i], L[i] = d, l
        if d == "L":
            j = bisect_left(rows_d.setdefault(r, []), c)
            tc = -1 if j == 0 or len(rows_d[r]) == 0 else rows_d[r][j - 1]
            c = (c - l) if (c - l > tc + 1) else (tc + 1)
        elif d == "R":
            j = bisect_right(rows_d.setdefault(r, []), c)
            tc = W if j == len(rows_d[r]) else rows_d[r][j]
            c = (c + l) if c + l < tc - 1 else (tc - 1)
        elif d == "U":
            j = bisect_left(cols_d.setdefault(c, []), r)
            tr = -1 if j == 0 or len(cols_d[c]) == 0 else cols_d[c][j - 1]
            r = (r - l) if r - l > tr + 1 else (tr + 1)
        else:
            assert d == "D"
            j = bisect_right(cols_d.setdefault(c, []), r)
            tr = H if j == len(cols_d[c]) else cols_d[c][j]
            r = (r + l) if r + l < tr - 1 else (tr - 1)
        print(r + 1, c + 1)


if __name__ == "__main__":
    main()
