#!/usr/bin/env python3

input()
N = [int(e) for e in input().split()]

min_total = float("Inf")
for x in range(1, 101):
    min_total = min(min_total, sum((x-y)**2 for y in N))
print(min_total)
