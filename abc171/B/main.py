#!/usr/bin/env python3

k = int(input().split()[1])
print(sum(sorted([int(e) for e in input().split()])[:k]))


