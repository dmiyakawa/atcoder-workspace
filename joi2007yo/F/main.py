#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    n = int(input())
    X = {tuple(map(int, input().split())) for _ in range(n)}
    dp = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if (x, y) in X:
                dp[x][y] = 0
            elif (x, y) == (1, 1):
                dp[x][y] = 1
            else:
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
    # from pprint import pprint
    # print(X)
    # pprint(dp)
    print(dp[a][b])


if __name__ == "__main__":
    main()
