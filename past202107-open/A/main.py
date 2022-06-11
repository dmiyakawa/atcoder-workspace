#!/usr/bin/env python3
S = input()

c = (sum(int(e) * 3 for e in S[:14:2]) + sum(int(e) for e in S[1:14:2])) % 10
print("Yes" if c == int(S[14]) else "No")
