#!/usr/bin/env python3

N, A, B, C, D, E = [int(input()) for _ in range(6)]
m = min(A, B, C, D, E)
print(N // m + (1 if N % m else 0) + 4)
