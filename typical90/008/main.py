#!/usr/bin/env python3
from typing import List, Dict

MOD = 1000000007  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


def solve(N: int, S: str):
    # atcoderのi文字目読み込んだ状態がn種類ある
    dp: List[Dict[int, int]] = []
    for i, ch in enumerate(S):
        if i == 0:
            dp.append({1: 1} if ch == "a" else {})
        else:
            new_d = dp[i - 1].copy()
            dp.append(new_d)
            if ch == "a":
                new_d[1] = (dp[i - 1].get(1, 0) + 1) % MOD
            elif ch == "t":
                new_d[2] = (dp[i - 1].get(1, 0) + dp[-1].get(2, 0)) % MOD
            elif ch == "c":
                new_d[3] = (dp[i - 1].get(2, 0) + dp[-1].get(3, 0)) % MOD
            elif ch == "o":
                new_d[4] = (dp[i - 1].get(3, 0) + dp[-1].get(4, 0)) % MOD
            elif ch == "d":
                new_d[5] = (dp[i - 1].get(4, 0) + dp[-1].get(5, 0)) % MOD
            elif ch == "e":
                new_d[6] = (dp[i - 1].get(5, 0) + dp[-1].get(6, 0)) % MOD
            elif ch == "r":
                new_d[7] = (dp[i - 1].get(6, 0) + dp[-1].get(7, 0)) % MOD
    print(dp[N - 1][7], end="")


if __name__ == "__main__":
    main()
