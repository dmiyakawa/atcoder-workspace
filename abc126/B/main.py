#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def is_yy(_):
    return True


def is_mm(val):
    return 1 <= val <= 12


def main():
    S = input().rstrip()

    a, b = int(S[:2]), int(S[2:])
    if is_yy(a) and is_mm(b):
        if is_mm(a) and is_yy(b):
            return "AMBIGUOUS"
        else:
            return "YYMM"
    else:
        if is_mm(a) and is_yy(b):
            return "MMYY"
        else:
            return "NA"


if __name__ == "__main__":
    print(main())
