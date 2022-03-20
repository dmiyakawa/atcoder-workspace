#!/usr/bin/env python3


MOD = 1000000007  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)


def solve(N: int, L: int):
    dp = [1]
    for n in range(1, N + 1):
        if n < L:
            dp.append(dp[n - 1])
        else:
            dp.append((dp[n - 1] + dp[n - L]) % MOD)
    print(dp[N], end="")


if __name__ == "__main__":
    main()
