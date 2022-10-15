#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [int(e) for e in next(tokens)]  # type: List[int]
    X = next(tokens)  # type: str
    assert len(S) == len(X) == N
    solve(N, S, X)


def solve(N: int, S: "List[int]", X: str):
    dp = [[False] * 7 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        is_takahashi = X[i] == "T"
        if i == N - 1:
            if is_takahashi:
                for r in range(7):
                    dp[i][r] = r % 7 == 0 or (r + S[i]) % 7 == 0
            else:
                dp[i][0] = S[i] % 7 == 0
        else:
            for r in range(7):
                a = dp[i + 1][r * 10 % 7]
                b = dp[i + 1][(r + S[i]) * 10 % 7]
                if is_takahashi:
                    dp[i][r] = a or b
                else:
                    dp[i][r] = a and b

    print("Takahashi" if dp[0][0] else "Aoki")


def solve_tle(N: int, S: "List[int]", X: str):

    cache = {}

    def _check(i, prev_r):
        print(f"_check({i}, {prev_r})")
        is_takahashi = X[i] == "T"
        if i == N - 1:
            if is_takahashi:
                return prev_r % 7 == 0 or (prev_r + S[i]) % 7 == 0
            else:
                return prev_r % 7 == 0 and (prev_r + S[i]) % 7 == 0
        else:
            ra, rb = prev_r * 10 % 7, (prev_r + S[i]) * 10 % 7
            aa = cache.setdefault((i + 1, ra), _check(i + 1, ra))
            ab = cache.setdefault((i + 1, rb), _check(i + 1, rb))
            if is_takahashi:
                return aa or ab
            else:
                return aa and ab

    print("Takahashi" if _check(0, 0) else "Aoki")


if __name__ == "__main__":
    main()
