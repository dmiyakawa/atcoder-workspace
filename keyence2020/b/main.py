#!/usr/bin/env python3

N = int(input())
XL = [tuple(int(e) for e in input().split()) for _ in range(N)]

p = sorted([(XL[i][0] - XL[i][1], XL[i][0] + XL[i][1]) for i in range(N)], key=lambda x: x[1])

cur = float('-inf')
count = 0
for i in range(N):
    if cur <= p[i][0]:
        count += 1
        cur = p[i][1]

print(count)

