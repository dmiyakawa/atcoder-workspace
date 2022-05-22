#!/usr/bin/env python3
x1, y1, x2, y2 =[int(e) for e in input().split()]

def neighbors(x, y):
    ret = set()
    for i, j in [(1, 2), (2, 1)]:
        ret.add((x + i, y + j))
        ret.add((x - i, y + j))
        ret.add((x + i, y - j))
        ret.add((x - i, y - j))
    return ret

# print(neighbors(x1, y1))
# print(neighbors(x2, y2))
print("Yes" if neighbors(x1, y1) & neighbors(x2, y2) else "No")
