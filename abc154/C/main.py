#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "YES"  # type: str
NO = "NO"  # type: str


def main():
    N = int(input())
    A_set = {int(e) for e in input().split()}
    print(YES if len(A_set) == N else NO)


if __name__ == "__main__":
    main()
