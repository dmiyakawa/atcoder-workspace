#!/usr/bin/env python3

lst = []
for _ in range(4):
    line = input().split()
    line.reverse()
    lst.append(line)

lst.reverse()

for line in lst:
    print(" ".join(line))
