#!/usr/bin/env python3

N = int(input())

s = N % 60
rem = N // 60
m = rem % 60
h = rem // 60
print("{:02d}:{:02d}:{:02d}".format(h, m, s))
