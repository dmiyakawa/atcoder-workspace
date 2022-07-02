#!/usr/bin/env python3
from collections import defaultdict


def main():
    N, Q = map(int, input().split())
    A = [int(e) for e in input().split()]
    d = defaultdict(list)
    for i, a in enumerate(A):
        d[a].append(i)
    for _ in range(Q):
        x, k = [int(e) for e in input().split()]
        k -= 1
        lst = d[x]
        if k >= len(lst):
            print(-1)
        else:
            print(lst[k] + 1)


if __name__ == "__main__":
    main()
