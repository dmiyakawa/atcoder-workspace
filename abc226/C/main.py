#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():
    from functools import reduce
    N = int(input())
    costs = []
    required = {}
    for i in range(N):
        lst = [int(e) for e in input().split()]
        t, k = lst[0], lst[1]
        costs.append(t)
        required[i] = set(i - 1 for i in lst[2:])
    # print(required)
    to_be_processed = required[N - 1].copy()
    total_cost = costs[N - 1]
    processed = {N - 1}
    while to_be_processed:
        i = to_be_processed.pop()
        if i in processed:
            continue
        processed.add(i)
        to_be_processed |= required[i]
        # print(total_cost, i, costs[i], total_cost + costs[i])
        total_cost += costs[i]
    print(total_cost)


if __name__ == "__main__":
    main()
