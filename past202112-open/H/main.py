#!/usr/bin/env python3

def main():
    S = input()
    T = input()
    dp = []
    for i, s in enumerate(S):
        lst = []
        dp.append(lst)
        for j, t in enumerate(T):
            v = 1 if s != t else 0
            left = dp[i][j - 1] if j > 0 else 0
            up = dp[i - 1][j] if i > 0 else 0
            ul = dp[i - 1][j - 1] + v if i > 0 and j > 0 else v
            lst.append(max(left, up, ul))

    print(dp[len(S) - 1][len(T) - 1])


if __name__ == "__main__":
    main()
