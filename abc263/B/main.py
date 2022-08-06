#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, P: "List[int]"):
    links = {}
    for i, p in enumerate(P, start=2):
        links[i] = p
    count = 0
    n = N
    while True:
        count += 1
        next_n = links[n]
        if next_n == 1:
            break
        n = next_n
    print(count)


def main():
    N = int(input())
    P = [int(e) for e in input().split()]
    solve(N, P)


if __name__ == "__main__":
    main()
