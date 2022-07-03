#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    N, Q = map(int, input().split())
    S = input()
    i = 0
    for _ in range(Q):
        t, x = [int(e) for e in input().split()]
        if t == 1:
            i = (i + N - x) % N
        else:
            print(S[(i + x - 1) % N])


if __name__ == "__main__":
    main()
