#!/usr/bin/env python3

MOD = 1000000007  # type: int

def solve_2(N: int, P: int):
    print((P - 1) * pow(P - 2, N - 1, MOD) % MOD)


def solve(N: int, P: int):
    lst = [P - 2]
    n = 1
    while 2 ** n <= N:
        lst.append(lst[-1] ** 2 % MOD)
        n += 1
    ans = P - 1
    n = N - 1
    i = 0
    while n:
        if n & 1:
            ans *= lst[i]
            ans %= MOD
        n >>= 1
        i += 1
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve_2(N, P)


if __name__ == "__main__":
    main()
