#!/usr/bin/env python3

N = int(input())
B = [int(e) for e in input().split()]
B.append(B[-1])
A = [B[0]]
for i in range(1, N):
    A.append(min(B[i-1], B[i]))
print(sum(A))
