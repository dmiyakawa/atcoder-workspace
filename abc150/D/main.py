#!/usr/bin/env python3

import functools
import math


def solve_ref(N: int, M: int, A: "List[int]"):
    B = sorted(a // 2 for a in A)
    l = lcm_all(*B)
    for i in range(N):
        if (l // B[i]) % 2 == 0:
            print(0)
            return
    print(((M // l) + 1) // 2)


def lcm(a, b):
    """aとbの最小公倍数を求める"""
    return a // math.gcd(a, b) * b


def lcm_all(*args):
    """多引数版のlcm"""
    return functools.reduce(lcm, args)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_ref(N, M, a)


if __name__ == "__main__":
    main()
