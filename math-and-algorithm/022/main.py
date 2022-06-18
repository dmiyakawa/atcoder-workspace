#!/usr/bin/env python3

from collections import Counter


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    counter = Counter(A)
    ans = 0
    for n in range(1, 50000):
        ans += counter[n] * counter[100000 - n]
    ans += counter[50000] * (counter[50000] - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
