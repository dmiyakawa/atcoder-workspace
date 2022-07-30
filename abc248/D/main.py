#!/usr/bin/env python3

import bisect
from collections import defaultdict


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    Q = int(input())
    d = defaultdict(list)
    for i, a in enumerate(A):
        d[a].append(i)
    for _ in range(Q):
        l, r, x = map(int, input().split())
        print(bisect.bisect_right(d[x], r - 1) - bisect.bisect_left(d[x], l - 1))



if __name__ == "__main__":
    main()
