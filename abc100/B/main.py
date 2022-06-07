#!/usr/bin/env python3

D, N = [int(e) for e in input().split()]

if N == 100:
    if D == 0:
        print(101)
    elif D == 1:
        print(10100)
    else:
        print(1010000)
else:
    print(N * 100**D)
