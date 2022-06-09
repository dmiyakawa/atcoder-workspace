#!/usr/bin/env python3

N, M = [int(e) for e in input().split()]

l, r = 0, N
for _ in range(M):
    L, R = [int(e) for e in input().split()]
    l = max(l, L)
    r = min(r, R)

if l <= r:
    print(r - l + 1)
else:
    print(0)
