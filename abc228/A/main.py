#!/usr/bin/env python3

S, T, X = [int(e) for e in input().split()]

print("Yes" if S <= X < T or T < S <= X or X < T < S else "No") 
