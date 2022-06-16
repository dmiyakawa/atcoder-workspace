#!/usr/bin/env python3

N, S = map(int, input().split())

count = 0
for r in range(1, N + 1):
    for b in range(1, N + 1):
        if r + b <= S:
            count += 1
print(count)
