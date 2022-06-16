#!/usr/bin/env python3

import math


def main():
    N = int(input())
    s = set()
    for n in range(1, int(math.sqrt(N)) + 1):
        if N % n == 0:
            s.add(n)
            s.add(N // n)
    for i in s:
        print(i)


if __name__ == "__main__":
    main()
