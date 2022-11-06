#!/usr/bin/env python3


def solve(N: int, A: "List[int]"):
    min_2 = 10**9
    min_3 = 10**9
    A_primes = []
    noises = set()
    for a in A:
        if a == 1:
            primes = {}
        else:
            primes = factorize_in_prime(a)
        noises |= set(primes.keys()) - {2, 3}
        A_primes.append(primes)
        min_2 = min(min_2, primes.get(2, 0))
        min_3 = min(min_3, primes.get(3, 0))

    ans = 0
    for primes in A_primes:
        if noises - set(primes.keys()) - {2, 3}:
            print(-1)
            return
        ans += primes.get(2, 0) - min_2
        ans += primes.get(3, 0) - min_3
    print(ans)


def factorize_in_prime(n) -> "Dict[int, int]":
    """2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す"""
    # https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
    assert n >= 2
    d = {}
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                count += 1
                temp //= i
            d[i] = count

    if temp != 1:
        d[temp] = 1

    if not d:
        d[n] = 1

    return d

def _debug():
    import random
    N = 1000
    A = [random.randrange(10**8, 10**9) for _ in range(N)]
    solve(N, A)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    # _debug()
    main()

