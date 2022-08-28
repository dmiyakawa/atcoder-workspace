#!/usr/bin/env python3


def solve(N: int, T: "List[int]", X: "List[int]", A: "List[int]"):
    d = [[0] * 5 for _ in range(10**5 + 1)]
    for t, x, a in zip(T, X, A):
        d[t][x] += a

    dp = [[0] * 5 for _ in range(10**5 + 1)]
    for t in range(1, 10**5 + 1):
        for x in range(0, 5):
            if t < x:
                continue
            prev = max(dp[t - 1][x - 1] if x > 0 else 0, dp[t - 1][x], dp[t - 1][x + 1] if x < 4 else 0)
            dp[t][x] = prev + d[t][x]
    print(max(dp[10**5]))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, T, X, A)


if __name__ == "__main__":
    main()
