#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = float("inf")


def calc_min(lst, cur_cost):
    if len(lst) == 1:
        return cur_cost
    min_cost = Inf
    min_i = None
    for i in range(len(lst) - 1):
        cand_cost = lst[i] + lst[i + 1]
        if min_cost > cand_cost:
            min_i = i
            min_cost = cand_cost
    ret = Inf

    new_lst = lst[:min_i] + [lst[min_i] + lst[min_i + 1]] + lst[min_i + 2:]
    ret = min(ret, calc_min(new_lst, min_cost))
    return ret + cur_cost


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(calc_min(A, 0))


def _debug():
    import random
    A = [random.randint(1, 1) for _ in range(400)]
    print(calc_min(A, 0))


if __name__ == "__main__":
    # _debug()
    main()
