#!/usr/bin/env python3

N = int(input())
A = [int(elem) for elem in input().split()]
B = [int(elem) for elem in input().split()]
C = [int(elem) for elem in input().split()]

total_count = 0
for a_value in A:
    for b_value in B:
        for c_value in C:
            if (a_value + b_value + c_value) % 46 == 0:
                total_count += 1

print(total_count, end="")
