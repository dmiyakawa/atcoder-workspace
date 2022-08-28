#!/usr/bin/env python3



def solve(N: int):
    dp = [[0.0] * 7 for _ in range(N + 1)]

    for i in range(N, -1, -1):
        if i == N:
            e = 3.5
        else:
            e = sum(dp[i + 1][n] / 6 for n in range(1, 7))
        for n in range(0, 7):
            dp[i][n] = e if e > n else n
    print(dp[1][0])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
