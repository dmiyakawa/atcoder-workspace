#!/usr/bin/env python3

S, T = input().split()

s = -int(S[1:]) if S[0] == "B" else int(S[:1]) - 1
t = -int(T[1:]) if T[0] == "B" else int(T[:1]) - 1
print(abs(s - t))
