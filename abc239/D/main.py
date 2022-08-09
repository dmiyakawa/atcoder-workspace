#!/usr/bin/env python3

import sys

def solve(A: int, B: int, C: int, D: int):
    primes = set()
    for n in range(2, B + D + 1):
        if prime_check_by_miller_rabin(n):
            primes.add(n)

    for i in range(A, B + 1):
        all_not_prime = True
        for j in range(C, D + 1):
            if i + j in primes:
                all_not_prime = False
                break
        if all_not_prime:
            print("Takahashi")
            return
    print("Aoki")


def prime_check_by_miller_rabin(n: int):
    """ミラーラビン素数判定法を用いて与えられた正の整数が素数であるかを返す"""

    def _suspect(a, t, _n):
        x = pow(a, t, _n)
        n1 = _n - 1
        while t != n1 and x != 1 and x != n1:
            x = pow(x, 2, _n)
            t <<= 1
        return t & 1 or x == n1

    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    check_list = (2, 7, 61) if n < 2 ** 32 else (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for i in check_list:
        if i >= n:
            break
        if not _suspect(i, d, n):
            return False
    return True


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)





if __name__ == "__main__":
    main()
