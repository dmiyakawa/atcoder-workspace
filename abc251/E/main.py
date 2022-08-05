#!/usr/bin/env python3

import sys


def solve(N: int, A: "List[int]"):
    cand = []
    for j in range(2):
        dp = [[0 for _ in range(2)] for _ in range(N)]
        for i in range(N):
            if i == 0:
                dp[i][0] = A[-1] if j == 1 else 0
                dp[i][1] = A[0]
            elif i < N - 1:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]
            else:
                dp[i][0] = dp[i - 1][1] + (A[i] if j == 0 else 0)
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]
        cand.extend(dp[N - 1])

    print(min(cand))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)





if __name__ == "__main__":
    main()
