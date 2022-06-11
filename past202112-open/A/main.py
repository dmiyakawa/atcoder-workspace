#!/usr/bin/env python3

H, W = [int(e) for e in input().split()]
h, w = [int(e) for e in input().split()]

print("Yes" if h >= H and w <= W else "No")
