#!/usr/bin/env python3
#
# 繰り返し二乗法
# https://yukicoder.me/problems/no/16
#

import math
import unittest


def repeated_squaring_sum(x, A, p):
    """(x^A1 + x^A2 ... + x^An) mod p を求める"""
    a_max = int(math.log2(max(A))) + 1
    cache = [1, x]
    i = 2
    while i <= a_max:
        cache.append((cache[i - 1] ** 2) % p)
        i += 1
    total = 0
    for a in A:
        b = format(a, "b")
        sq = 1
        for i in range(len(b)):
            if b[i] == "1":
                sq = sq * cache[len(b) - i] % p
        total = (total + sq) % p
    return total


class RepeatedSquaringTest(unittest.TestCase):
    def test_1(self):
        MOD = 1_000_003
        self.assertEqual(14, repeated_squaring_sum(2, [1, 2, 3], MOD))
        self.assertEqual(253110, repeated_squaring_sum(2, [0, 100], MOD))


def main():
    import sys
    MOD = 1_000_003
    if len(sys.argv) > 2:
        x = int(sys.argv[1])
        A = [int(e) for e in sys.argv[2:]]
        print(f"x: {x}, A: {A}", file=sys.stderr)
    else:
        x, N = map(int, input().split())
        A = [int(e) for e in input().split()]
    print(repeated_squaring_sum(x, A, MOD))


if __name__ == "__main__":
    main()
