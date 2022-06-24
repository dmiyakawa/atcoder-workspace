#!/usr/bin/env python3

def main():
    N = int(input())
    A = [0] + [int(e) for e in input().split()]
    dp = {1: A[1], 2: A[2]}
    for n in range(3, N + 1):
        dp[n] = max(dp[n - 1], dp[n - 2] + A[n])
    print(dp[N])


if __name__ == "__main__":
    main()
