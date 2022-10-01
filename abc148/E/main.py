#!/usr/bin/env python3
import math


def solve(N: int):
    if N % 2 == 1:
        print(0)
        return
    M = math.ceil(math.log10(N))
    dp = [0] * (M + 1)
    for i in range(1, M + 1):
        dp[i] = 10 * dp[i - 1] + 10**i // 2


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
