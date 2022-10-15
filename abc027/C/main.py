#!/usr/bin/env python3

import sys
from functools import lru_cache


def solve(N: int):
    m = 0
    ac = 0
    while True:
        M = 4**m
        if N < ac + M:
            return True
        elif N < ac + 2 * M:
            return False
        ac += 2 * M
        m += 1


def solve_wa(N: int):

    @lru_cache(10**5)
    def _f(n, is_takahashi):
        if 2 * n > N and 2 * n + 1 > N + 1:
            return not is_takahashi
        r1 = _f(2 * n, not is_takahashi)
        r2 = _f(2 * n + 1, not is_takahashi)
        if r1 == is_takahashi or r2 == is_takahashi:
            return is_takahashi
        else:
            return not is_takahashi

    return _f(1, True)
    # print(N, "Takahashi" if _f(1, True) else "Aoki")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int

    print("Takahashi" if solve(N) else "Aoki")


def _debug():
    p = None
    pn = 0
    for n in range(1, 10000):
        ret = solve(n)
        if p != ret:
            print(n, n - pn, ret)
            p = ret
            pn = n


if __name__ == "__main__":
    main()
