#!/usr/bin/env python3

import math


def solve(A, B, C) -> str:
    if A == B == 0:
        return "="
    if A == 0:
        return "<" if B > 0 or C % 2 == 0 else ">"
    if B == 0:
        return ">" if A > 0 or C % 2 == 0 else "<"
    a = (A // abs(A))**C * math.log(abs(A)) * C
    b = (B // abs(B))**C * math.log(abs(B)) * C
    return "=" if a == b else (">" if a > b else "<")


def main():
    A, B, C = map(int, input().split())
    print(solve(A, B, C))


def check():
    import random
    for _ in range(10000):
        solve(random.randint(-100, 100), random.randint(-100, 100), random.randint(0, 100))


if __name__ == "__main__":
    main()
    # check()


