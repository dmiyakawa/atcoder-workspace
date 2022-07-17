#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    S = input()
    total = 0
    for i, s in enumerate(S):
        num_us = len(S) - i - 1
        num_ls = i
        if s == "U":
            total += num_us + 2 * num_ls
        else:
            total += 2 * num_us + num_ls
    print(total)


if __name__ == "__main__":
    main()
