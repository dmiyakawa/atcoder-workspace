#!/usr/bin/env python3

from fractions import Fraction
from typing import Dict

MOD = 998244353  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, K, W)


def solve(N: int, M: int, K: int, W: "List[int]"):
    # N種類の賞品、くじK回でM種類の賞品が得られる確率
    if M > K:
        print(0, end="")
        return
    w_total = sum(W)
    # K -> M -> Mの内訳 -> 確率
    dp: Dict[int, Dict[int, Dict[str, Fraction]]] = {}
    # K = 1, M = 1
    for i in range(N):
        key = "0" * i + "1" + "0" * (N - i - 1)
        dp.setdefault(1, {}).setdefault(1, {})[key] = Fraction(W[i], w_total)
    if M >= 2:
        print(f"N: {N}, M: {M}, K: {K}, W: {W}, W_total: {w_total}, dp: {dp}")
        for k in range(2, K + 1):
            for m in range(1, min(M + 1, k + 1)):
                # くじを k 回引いたときに m 種類から選ばれているパターン
                dp.setdefault(k, {})[m] = new_d = {}
                # k - 1 で m 種類選ばれている状態からm種類選ばれている状態を維持するパターン
                if k - 1 >= m:
                    for key, fraction in dp[k - 1][m].items():
                        new_d[key] = Fraction(sum(z[0] for z in zip(W, key) if z[1] == "1"), w_total) * fraction
                if m > 1:
                    # k - 1 で m - 1 種類選ばれている状態からm種類選ばれている状態に変化するパターン
                    for key, fraction in dp[k - 1][m - 1].items():
                        for i, z in enumerate(zip(W, key)):
                            if z[1] == "1":
                                continue
                            new_key = key[:i] + "1" + key[(i + 1):]
                            new_d[new_key] = Fraction(sum(z[0] for z in zip(W, key) if z[1] == "1"), w_total) * fraction
    print(f"N: {N}, M: {M}, K: {K}, W: {W}, W_total: {w_total}, dp: {dp}")
    p_1 = sum(dp[K][M].values())
    num, den = p_1.numerator, p_1.denominator
    print(p_1)
    i = 0
    while (num + MOD * 2) % den:
        i += 1
    print((num + MOD * 2) // den)


if __name__ == "__main__":
    main()
