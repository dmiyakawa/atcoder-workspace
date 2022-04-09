#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():
    lst = [ch for ch in input().rstrip() if ch not in "aoeiu"]
    print("".join(lst))


if __name__ == "__main__":
    main()
