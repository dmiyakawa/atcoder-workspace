#!/usr/bin/env python3



def solve(H: int, N: int, A: "List[int]", B: "List[int]"):
    dp = [-1] * (H + 1)
    dp[H] = 0
    for h in range(H, -1, -1):
        # print(h, dp, dp[h])
        if dp[h] < 0:
            continue
        for a, b in zip(A, B):
            v = 0 if (h - a <= 0) else (h - a)
            if dp[v] < 0 or dp[v] > dp[h] + b:
                dp[v] = dp[h] + b
    print(dp[0])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(H, N, A, B)


if __name__ == "__main__":
    main()
