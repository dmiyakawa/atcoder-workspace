#!/usr/bin/env python3
H, W = [int(e) for e in input().split()]
lst = []

for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "o":
            lst.append((i, j))

print(abs(lst[0][0] - lst[1][0]) + abs(lst[0][1] - lst[1][1]))
