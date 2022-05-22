#!/usr/bin/env python3
N, K = [int(e) for e in input().split()]
A = [int(e) for e in input().split()]
B = [int(e) - 1 for e in input().split()]
max_score = sorted(A, reverse=True)[0]
possible = False
for i, a in enumerate(A):
    if a == max_score and i in B: 
        possible = True
        break
print("Yes" if possible else "No")
