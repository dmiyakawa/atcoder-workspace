#!/usr/bin/env python3

N, K = [int(e) for e in input().split()]

d = {}
for _ in range(N):
    a, b = [int(e) for e in input().split()]
    d[a] = d.get(a, 0) + b

lst = sorted(d.items())

for a, b in lst:
    if K <= b:
        print(a)
        break
    else:
        K -= b
