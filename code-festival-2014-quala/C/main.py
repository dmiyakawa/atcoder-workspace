#!/usr/bin/env python3

A, B = [int(e) for e in input().split()]

a1 = (A - 1) // 4
a2 = (A - 1) // 100
a3 = (A - 1) // 400
b1 = B // 4
b2 = B // 100
b3 = B // 400

print((b1 - b2 + b3) - (a1 - a2 + a3))
