#!/usr/bin/env python3
A, B = [int(e) for e in input().split()]
print("Yes" if A * B % 2 == 1 else "No")
