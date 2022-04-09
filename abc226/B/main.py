#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():
    N = int(input())
    L = [[int(e) for e in input().split()[1:]] for _ in range(N)]
    L.sort()
    count = 1
    for i in range(1, N):
        if L[i - 1] != L[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
