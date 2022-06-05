#!/usr/bin/env python3

N = int(input())

lst = []
for n in range(1, N + 1):
    prev_lst = lst
    lst = []
    for i in range(n):
        if i == 0 or i == n - 1:
            lst.append(1)
        else:
            lst.append(prev_lst[i - 1] + prev_lst[i])
    print(" ".join(str(value) for value in lst))

