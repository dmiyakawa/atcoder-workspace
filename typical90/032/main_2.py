#!/usr/bin/env python3
#
# 感想:
# N! = 10! が十分小さいのでpermutationを全部舐めてもOKだった……
#
# - PyPy3 -> AC
# - Python3 (CPython) -> TLE
#

import itertools
import sys

N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append([int(elem) for elem in sys.stdin.readline().split()])
M = int(sys.stdin.readline())

ng_combinations = set()
for _ in range(M):
    ng_combinations.add(tuple(int(elem) for elem in sys.stdin.readline().split()))

min_score = -1
for perm in itertools.permutations(list(range(1, N + 1))):
    total_score = A[perm[0] - 1][0]
    possible = True
    for i in range(1, N):
        if (min(perm[i - 1], perm[i]), max(perm[i - 1], perm[i])) in ng_combinations:
            possible = False
            break
        total_score += A[perm[i] - 1][i]
    if not possible:
        continue
    if min_score == -1 or min_score > total_score:
        min_score = total_score

print(min_score, end="")

