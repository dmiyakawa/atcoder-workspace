#!/usr/bin/env python3
import math
import time


def main():
    t, N = map(int, input().split())
    m = math.ceil(100 * N / t)
    while int(t * m / 100) >= N:
        m -= 1
    prev = None
    for l in range(m + 1, 0, -1):
        val = int(l * (100 + t) / 100)
        if prev is not None and prev - val > 1:
            print(prev - 1)
            break
        prev = val


if __name__ == "__main__":
    main()
