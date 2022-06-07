#!/usr/bin/env python3

x1, y1, x2, y2 = [int(e) for e in input().split()]

a, b = x2 - x1, y2 - y1

x4, y4 = -b + x1, a + y1
x3, y3 = a - b + x1, a + b + y1

print(x3, y3, x4, y4)
