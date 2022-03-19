#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


def eratosthenes(n):
    """エラトステネスのふるいの結果を[0, n)範囲のList[bool]で返す"""
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for p in range(2, n + 1):
        if not is_prime[p]:
            continue
        q = p * 2
        while q <= n:
            is_prime[q] = False
            q += p

    return is_prime


def solve(N: int):
    import math
    N_sqrt = math.floor(math.sqrt(N)) + 1
    multiples = []
    m = N
    for n, is_prime in enumerate(eratosthenes(N_sqrt)):
        if not is_prime:
            continue
        while m > 1 and m % n == 0:
            multiples.append(n)
            m = m // n

    if m != 1 and m != N:
        multiples.append(m)

    import sys
    print(N, multiples, file=sys.stderr)
    num_multiples = len(multiples)
    print(math.ceil(math.log2(num_multiples)) if num_multiples > 0 else 0, end="")


if __name__ == "__main__":
    main()
