#!/usr/bin/env python3
from collections import Counter


def main():
    _, K = map(int, input().split())
    A = [int(e) for e in input().split()]
    B = A.copy()
    for i in range(1, len(A)):
        B[i] += B[i - 1]

    counter = Counter(B)
    count = 0
    for i, b in enumerate(B):
        if b == K:
            count += 1
        counter[b] -= 1
        count += counter[b + K]

    print(count)


if __name__ == "__main__":
    main()
