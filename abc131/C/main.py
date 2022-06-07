#!/usr/bin/env python3

import math


def lcm(a, b):
    """aとbの最小公倍数を求める"""
    return a // math.gcd(a, b) * b


def main():
    A, B, C, D = [int(e) for e in input().split()]
    total = B - A + 1
    x = B // C - (A - 1) // C
    y = B // D - (A - 1) // D
    xy = B // lcm(C, D) - (A - 1) // lcm(C, D)
    print(total - (x + y - xy))


if __name__ == "__main__":
    main()
