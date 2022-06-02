#!/usr/bin/env python3

N, K = [int(e) for e in input().split()]
R = [int(e) for e in input().split()]

R.sort()

rate = 0
for i, r in enumerate(R[-K:]):
    rate += r / 2**(K-i)

print(rate)


