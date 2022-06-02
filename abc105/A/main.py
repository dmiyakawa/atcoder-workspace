#!/usr/bin/env python3

N, K = [int(e) for e in input().split()]

print(1 if N % K > 0 else 0)
