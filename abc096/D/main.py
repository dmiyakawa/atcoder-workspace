#!/usr/bin/env python3
from itertools import combinations


def solve(N: int):
    primes_all = list_primes(55555*5)
    primes_all_set = set(primes_all)
    primes = [p for p in primes_all if p <= 55555]
    primes_set = set(primes)
    print(len(primes_all_set))
    print(len(primes_set))


def list_primes(n):
    """nまでの素数をエラトステネスの篩を用いて求める（nを含む）"""
    ret = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(n + 1):
        if not is_prime[i]:
            continue
        ret.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

    return ret


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
