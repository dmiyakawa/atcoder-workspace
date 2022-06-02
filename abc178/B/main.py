#!/usr/bin/env python3
a, b, c, d = [int(e) for e in input().split()]

print(max(a * c, a * d, b * c, b * d))
