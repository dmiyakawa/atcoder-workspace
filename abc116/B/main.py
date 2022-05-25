#!/usr/bin/env python3
n = int(input())

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

a = {n}

i = 1
while True:
    n = f(n)
    i += 1
    if n in a:
        break
    a.add(n)
print(i) 
