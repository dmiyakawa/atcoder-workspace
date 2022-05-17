#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    S = input()
    s = S
    while len(s) < 6:
        s += S
    print(s)


if __name__ == "__main__":
    main()
