#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int):
    # a + b = K + c + d
    count = 0
    # 2 <= c + d <= 2N
    for n in range(2, 2*N + 1):
        # a + b = K + n, n = c + d
        if K + n > 2 * N:
            break
        a = max(2 * N - K - n + 1, 0) if K + n - 1 >= N else max(K + n - 1, 0)
        b = 2 * N - n + 1 if n - 1 >= N else n - 1
        count += a * b
    print(count)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == "__main__":
    main()
