#!/usr/bin/env python3

import sys
from typing import List, Optional

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")
MOD = 10 ** 9 + 7
MOD2 = 998244353


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)


def solve(s: str, t: str):
    dp: List[List[int]] = [[0] * (len(t) + 1)]
    for i in range(1, len(s) + 1):
        dp.append(dp[i - 1].copy())
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    length = dp[len(s)][len(t)]
    ans: List[Optional[str]] = [None] * length
    cur_s, cur_t = len(s), len(t)
    while length > 0:
        if s[cur_s - 1] == t[cur_t - 1]:
            ans[length - 1] = t[cur_t - 1]
            length -= 1
            cur_s -= 1
            cur_t -= 1
        elif dp[cur_s - 1][cur_t] == dp[cur_s][cur_t]:
            cur_s -= 1
        else:
            cur_t -= 1
    print("".join(ans))


if __name__ == "__main__":
    main()
