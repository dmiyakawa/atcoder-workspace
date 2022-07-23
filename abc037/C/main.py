#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, a: "List[int]"):
    B = a.copy()
    for i in range(1, N):
        B[i] += B[i - 1]
    ans = 0
    for i in range(N - K + 1):
        ans += B[i + K - 1] - (B[i - 1] if i > 0 else 0)
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)


if __name__ == "__main__":
    main()
