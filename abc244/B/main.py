#!/usr/bin/env python3

N = int(input())
T = input().rstrip()

x, y = 0, 0
dx, dy = 1, 0
for t in T:
    if t == "S":
        x, y = x + dx, y + dy
    else:
        if (dx, dy) == (1, 0):
            dx, dy = 0, -1
        elif (dx, dy) == (0, -1):
            dx, dy = -1, 0
        elif (dx, dy) == (-1, 0):
            dx, dy = 0, 1
        else:
            dx, dy = 1, 0
print(x, y, end="")
