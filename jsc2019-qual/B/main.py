#!/usr/bin/env python3

MOD = 1000000007  # type: int


def solve(N: int, K: int, A: "List[int]"):
    a = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                a += 1
    lst = [0, a]
    n = 2
    while n <= K:
        lst.append((lst[-1] * 2) % MOD)
        n *= 2
    ax = (a * K) % MOD

    b = 0
    for i in range(N):
        for j in range(N):
            if A[i] > A[j]:
                b += 1
    b %= MOD
    if K == 1:
        bx = 0
    else:
        bx = (b * comb(K, 2)) % MOD
    ans = (ax + bx) % MOD
    print(ans)


def comb(n, r):
    """nCr を計算する。 factorial(N) // factorial(N - r) // factorial(r) より概して高速"""
    from operator import mul
    from functools import reduce
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == "__main__":
    main()
