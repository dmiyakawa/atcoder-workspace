#!/usr/bin/env python3

def main():
    N, NG1, NG2, NG3 = int(input()), int(input()), int(input()), int(input())
    dp = {0: 100}
    for i in range(1, N + 1):
        if i in [NG1, NG2, NG3]:
            continue
        rest = max(dp.get(i - 1, 0), dp.get(i - 2, 0), dp.get(i - 3, 0), 0)
        if rest > 0:
            dp[i] = rest - 1

    print("YES" if N in dp else "NO")


if __name__ == "__main__":
    main()
