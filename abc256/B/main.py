#!/usr/bin/env python3

N = int(input())
A = [int(e) for e in input().split()]

s = set()
P = 0
for a in A:
    s.add(0)
    next_s = set()
    for l in s:
        next_l = l + a
        if next_l >= 4:
            P += 1
        else:
            next_s.add(next_l)
    s = next_s
print(P)
