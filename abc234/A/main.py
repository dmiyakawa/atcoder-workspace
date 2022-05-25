#!/usr/bin/env python3
t = int(input())

def f(x):
    return x**2 + 2 * x + 3

print(f(f(f(t) + t) + f(f(t))))
