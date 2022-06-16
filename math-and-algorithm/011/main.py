#!/usr/bin/env python3

N = int(input())

lst = [True for _ in range(N + 1)]
lst[0] = False

for n in range(2, N + 1):
    i = 2
    while i * n <= N:
        lst[i * n] = False
        i += 1

result = []
for n in range(2, N + 1):
    if lst[n]:
        result.append(str(n))
print(" ".join(result))
