#!/usr/bin/env python3

MOD = 1000000007  # type: int


def solve(N: int, M: int, A: "List[int]"):
    dp = [0] * (N + 1)
    dp[0] = 1
    s = set(A)
    for i in range(N + 1):
        if i - 1 >= 0 and (i - 1 not in s):
            dp[i] += dp[i - 1]
        if i - 2 >= 0 and (i - 2 not in s):
            dp[i] += dp[i - 2]
        dp[i] %= MOD
    print(dp[N] % MOD)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, a)


if __name__ == "__main__":
    main()
