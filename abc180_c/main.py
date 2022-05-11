#!/usr/bin/env python3

import math

N = int(input())

lst_head = []
lst_tail = []

for n in range(1, math.ceil(math.sqrt(N))):
    if N % n == 0:
        lst_head.append(n)
        lst_tail.append(N // n)

for n in lst_head:
    print(n)

for n in reversed(lst_tail):




