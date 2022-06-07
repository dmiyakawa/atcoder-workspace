#!/usr/bin/env python3

a, b = [int(e) for e in input().split()]

count = 0
for x in range(1, 13):
    if x * 30 + x > a * 30 + b:
        break
    count += 1
print(count)
