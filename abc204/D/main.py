#!/usr/bin/env python3

import math


def solve_2(N, T):
    S = sum(T)
    dp = [[False] * (S + 1) for _ in range(N)]
    for i, t in enumerate(T):
        dp[i][t] = True
        if i > 0:
            for s in range(S + 1):
                dp[i][s] = (s == t) or dp[i - 1][s] or (s - t >= 0 and dp[i - 1][s - t])

    for s in range(math.ceil(S / 2), S + 1):
        if dp[N - 1][s]:
            print(s)
            return


def solve(N, T):
    dp = [set() for _ in range(N)]
    for i, t in enumerate(T):
        if i == 0:
            dp[i].add(t)
        else:
            for ok in dp[i - 1]:
                dp[i].add(ok)
                dp[i].add(t)
                dp[i].add(ok + t)
    # print(dp[N - 1])
    print(min(v for v in dp[N - 1] if v >= math.ceil(sum(T) / 2)))


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    T = sorted(map(int, input().split()))
    solve_2(N, T)


if __name__ == "__main__":
    main()
