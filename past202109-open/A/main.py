#!/usr/bin/env python3
A, B, C, D = [int(e) for e in input().split()]

print(min(A + B - C, D))
