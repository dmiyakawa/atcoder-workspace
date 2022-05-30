#!/usr/bin/env python3
N, X = [int(e) for e in input().split()]
A = [int(e) - 1 for e in input().split()]
s = {X - 1}
n = X - 1

while True:
    next_n = A[n]
    if next_n in s:
        break
    else:
        s.add(next_n)
        n = next_n
print(len(s))
