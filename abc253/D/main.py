#!/usr/bin/env python3

import math
import sys


def lcm(a, b):
    """aとbの最小公倍数を求める"""
    return a // math.gcd(a, b) * b


def solve(N: int, A: int, B: int):
    C = lcm(A, B)
    Sn = N * (N + 1) // 2
    Na = N // A
    Sa = Na * (A + Na * A) // 2
    Nb = N // B
    Sb = Nb * (B + Nb * B) // 2
    Nc = N // C
    Sc = Nc * (C + Nc * C) // 2
    print(Sn - Sa - Sb + Sc)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)


if __name__ == "__main__":
    main()
