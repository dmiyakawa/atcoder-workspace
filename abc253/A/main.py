#!/usr/bin/env python3
A, B, C = [int(e) for e in input().split()]

print("Yes" if A <= B <= C or C <= B <= A  else "No")

