#!/usr/bin/env python3
#
# https://atcoder.jp/contests/abc243/submissions/30086960
#

def sqrt(n):
    m = int(n**0.5)
    if m*m > n: m -= 1
    if (m+1)**2 <= n: m += 1
    return m


def calc(T, X):
    ans = []
    dp = [(0, 0), (1, 0)]
    for i in range(2, 10**5):
        dp.append((dp[-1][0]+dp[sqrt(i)][0], \
            dp[-1][1]+dp[-1][0]*(i**2-(i-1)**2)))
    for i in range(T):
        x = sqrt(X[i])
        y = sqrt(x)
        ans.append(dp[y][1]+dp[y][0]*(x-y*y+1))
    return ans


def main():
    import sys
    T = int(sys.stdin.readline())
    X = []
    for i in range(T):
        X.append(int(sys.stdin.readline()))
    print(*calc(T, X), sep="\n")


if __name__ == "__main__":
    main()
