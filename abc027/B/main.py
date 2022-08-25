#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]"):
    sum_a = sum(A)
    if sum_a % N != 0:
        return -1
    ave = sum_a // N
    rem = 0
    ans = 0
    for i, a in enumerate(A):
        rem = rem + a - ave
        if rem != 0:
            ans += 1
    return ans


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(solve(N, A))


if __name__ == "__main__":
    main()
