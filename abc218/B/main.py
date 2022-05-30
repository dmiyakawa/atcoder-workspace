#!/usr/bin/env python3

from string import ascii_lowercase
P =  [int(e) for e in input().split()]

lst = []
for p in P:
    lst.append(ascii_lowercase[p-1])
print("".join(lst))
