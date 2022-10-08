#!/usr/bin/env python3

from itertools import combinations, product


def solve(N: str, K: int):
    if len(N) < K:
        print(0)
        return
    int_N = int(N)
    ans = (int(N[0]) - 1) * comb(len(N) - 1, K - 1) * 9**(K - 1)
    if len(N) == 1:
        ans += 1
    else:
        if len(N) > K:
            ans += comb(len(N) - 1, K) * 9 ** K

        base = int(N[0]) * 10 ** (len(N) - 1)
        for c in combinations(range(len(N) - 1), K - 1):
            for p in product(*[range(1, 10) for _ in range(K - 1)]):
                v = base
                for i, n in enumerate(c):
                    v += p[i] * 10**n
                if v <= int_N:
                    ans += 1
                # print(v, v <= int_N, ans, "", c, p)
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

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == "__main__":
    main()
