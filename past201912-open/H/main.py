#!/usr/bin/env python3

import sys
from typing import List, Optional, Any

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    N = int(input())
    C: List[Optional[int]] = [int(e) for e in input().split()]
    Q = int(input())
    C.insert(0, None)

    all_min = Inf
    all_sold = 0
    odd_min = Inf
    odd_sold = 0
    parts_sold = 0
    for i, c in enumerate(C[1:], start=1):
        all_min = min(all_min, c)
        if i % 2 == 1:
            odd_min = min(odd_min, c)

    # print([n - all_sold - (odd_sold if i % 2 == 1 else 0) for i, n in enumerate(C[1:], start=1)])
    for i in range(Q):
        # print()
        # print(f"all_sold: {all_sold}, odd_sold: {odd_sold}, all_min: {all_min}, odd_min: {odd_min}")
        s = [int(e) for e in input().split()]
        if s[0] == 1:
            x, a = s[1], s[2]
            sold = all_sold + (odd_sold if x % 2 == 1 else 0)
            if a + sold < C[x]:
                C[x] -= a
                parts_sold += a
                if C[x] < all_min:
                    all_min = C[x]
                if x % 2 == 1 and C[x] < odd_min:
                    odd_min = C[x]
        elif s[0] == 2:
            a = s[1]
            if a + all_sold + odd_sold <= odd_min:
                odd_sold += a
        else:
            a = s[1]
            # print(a, all_sold, all_min)
            if a + all_sold <= all_min and a + all_sold + odd_sold <= odd_min:
                all_sold += a
        # print(i, s, all_sold, odd_sold, parts_sold)
        # print([n - all_sold - (odd_sold if i % 2 == 1 else 0) for i, n in enumerate(C[1:], start=1)])

    print(all_sold * N + odd_sold * (N // 2 + N % 2) + parts_sold)


if __name__ == "__main__":
    main()
