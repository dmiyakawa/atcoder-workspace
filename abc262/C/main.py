#!/usr/bin/env python3


def solve(N: int, A: "List[int]"):
    B = [a == n for n, a in enumerate(A, start=1)]
    Bc = B.count(True)
    count = comb(Bc, 2) if Bc >= 2 else 0
    for i, a in enumerate(A):
        if not B[i] and A[a - 1] == i + 1 and i < a - 1:
            count += 1

    print(count)


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

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
