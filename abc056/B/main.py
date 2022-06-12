#!/usr/bin/env python3

W, a, b = map(int, input().split())

a, b = min(a, b), max(a, b)
if a + W > b:
    print(0)
else:
    print(b - (a + W))

