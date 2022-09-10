#!/usr/bin/env python3



def solve(N: int, M: int, A: "List[int]"):
    dp = [[None] * (M + 1) for _ in range(N)]
    for i in range(N):
        dp[i][0] = 0

    for i, a in enumerate(A):
        for j in range(1, min(M + 1, i + 2)):
            lst = [dp[i - 1][j - 1] + j * a]
            if j < i + 1:
                lst.append(dp[i - 1][j])
            dp[i][j] = max(lst)

    # print(dp)
    print(dp[N - 1][M])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
