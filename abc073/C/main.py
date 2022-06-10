#!/usr/bin/env python3

N = int(input())
s = set()
for _ in range(N):
    n = int(input())
    if n in s:
        s.remove(n)
    else:
        s.add(n)
print(len(s))
