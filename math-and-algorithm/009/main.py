#!/usr/bin/env python3

N, S = [int(e) for e in input().split()]
A = sorted([int(e) for e in input().split()])

possible = set()

for a in A:
    next_possible = possible.copy()
    if a <= S:
        next_possible.add(a)
    for p in possible:
        if p + a <= S:
            next_possible.add(p + a)
    possible = possible.union(next_possible)

print("Yes" if S in possible else "No")


