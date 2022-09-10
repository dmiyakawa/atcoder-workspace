#!/usr/bin/env python3


def solve_2(N: int, A: "List[int]"):
    from operator import mul
    from functools import reduce
    ans = 0
    count = 0
    for i, a in enumerate(A):
        if i == 0 or A[i] > A[i - 1]:
            count += 1
        else:
            n = count + 1
            ans += reduce(mul, range(n, n - 2, -1)) // 2
            count = 1
    else:
        n = count + 1
        ans += reduce(mul, range(n, n - 2, -1)) // 2
    print(ans)



def solve(N: int, A: "List[int]"):
    prev_i = 0
    count = 0
    for i, a in enumerate(A):
        if i > 0 and A[i - 1] >= a:
            n = i - prev_i
            count += comb(n + 1, 2)
            prev_i = i
    n = N - prev_i
    count += comb(n + 1, 2)
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

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_2(N, a)


if __name__ == "__main__":
    main()
