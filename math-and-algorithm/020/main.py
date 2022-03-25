#!/usr/bin/env python3
import array

N = int(input())
A = array.array("l", [int(e) for e in input().split()])
count = 0
for i, a in enumerate(A):
    for j, b in enumerate(A[i + 1:], start=i + 1):
        if a + b > 1000:
            continue
        for k, c in enumerate(A[j + 1:], start=j + 1):
            if a + b + c > 1000:
                continue
            for l, d in enumerate(A[k + 1:], start=k + 1):
                if a + b + c + d > 1000:
                    continue
                for e in A[l + 1:]:
                    if a + b + c + d + e == 1000:
                        count += 1
print(count)
