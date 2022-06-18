#!/usr/bin/env python3

from collections import Counter
from itertools import permutations


def solve(S):
    if len(S) <= 3:
        for perm in permutations(S):
            if int("".join(perm)) % 8 == 0:
                return True
        return False
    c1 = Counter(S)
    d = []
    for n in range(112, 1000, 8):
        ns = str(n)
        if "0" in ns:
            continue
        c2 = Counter(ns)
        possible = True
        for ch, num in c2.items():
            if num > c1[ch]:
                possible = False
                break
        if possible:
            return True
    return False


def main():
    print("Yes" if solve(input()) else "No")


if __name__ == "__main__":
    main()
