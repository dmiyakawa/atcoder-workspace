#!/usr/bin/env python3

import math


def main():
    N = int(input())
    lst = []
    rem = N
    for n in range(2, int(math.sqrt(N)) + 1):
        if rem < n:
            break
        while rem % n == 0:
            lst.append(str(n))
            rem //= n
    if rem != 1:
        lst.append(str(rem))

    if not lst:
        lst.append(str(N))

    print(" ".join(lst))


if __name__ == "__main__":
    main()
