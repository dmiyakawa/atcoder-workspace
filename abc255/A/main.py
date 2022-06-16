#!/usr/bin/env python3

R, C = [int(e) - 1 for e in input().split()]
A = [[int(e) for e in input().split()] for _ in range(2)]
print(A[R][C])
