#!/usr/bin/env python3
import math


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    T = sorted(map(int, input().split()))

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


if __name__ == "__main__":
    main()
