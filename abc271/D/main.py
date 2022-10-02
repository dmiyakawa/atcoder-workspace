#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, S: int, A: "List[int]", B: "List[int]"):
    dp = [{} for _ in range(N + 1)]
    dp[0][S] = None
    for i, (a, b) in enumerate(zip(A, B), start=1):
        for rem in dp[i - 1].keys():
            if rem - a >= 0:
                dp[i][rem - a] = "H"
            if rem - b >= 0:
                dp[i][rem - b] = "T"
    # print(dp)
    if 0 in dp[N]:
        ans = []
        rem = 0
        for i in range(N, 0, -1):
            x = dp[i][rem]
            ans.append(x)
            if x == "H":
                rem += A[i - 1]
            else:
                rem += B[i - 1]
        print(YES)
        print("".join(reversed(ans)))
    else:
        print(NO)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, S, a, b)


if __name__ == "__main__":
    main()
