#!/usr/bin/env python3
N, A, B = [int(e) for e in input().split()]
for i in range(N):
    for a in range(A):
        lst = []
        for j in range(N):
            for b in range(B):
                lst.append("." if (i + j) % 2 == 0 else "#")
        print("".join(lst))

