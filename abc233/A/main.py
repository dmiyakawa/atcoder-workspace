#!/usr/bin/env python3

X, Y = [int(e) for e in input().split()]

if Y - X > 0:
    print((Y - X) // 10 + (1 if (Y - X) % 10 else 0))
else:
    print(0)
