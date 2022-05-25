#!/usr/bin/env python3
S = input()
a, b = [int(e) - 1 for e in input().split()]

print(S[:a]+S[b]+S[a+1:b]+S[a]+S[b+1:])
