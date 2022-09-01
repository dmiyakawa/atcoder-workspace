#!/usr/bin/env python3

from collections import defaultdict

MOD = 1000000007  # type: int


def solve(N: int, A: "List[List[int]]"):
    dp = [0] * 2**N
    dp[0] = 1

    # 1 が n bit 立っている数値を用いてDPを行いたいので辞書を作った
    #
    # solve_ref() のように素直に for n in range(1<<N) としても
    # 実は1の立っているbit数が少ない方から消費されるので、
    # 以下のように辞書を作らなくてもDPは成立する
    #
    # 同じことを itertools.combinations() でやるとTLE
    d = defaultdict(list)
    for n in range(2**N):
        # bin(n).count("1") や format(n, "b").count("1") もあり得るが相対的にはだいぶ遅い
        c = 0
        m = n
        while m:
            if m & 1:
                c += 1
            m = m >> 1
        d[c].append(n)

    for i in range(N):
        for j, a in enumerate(A[i]):
            if not a:
                continue
            for v in d[i]:
                if v & 1 << j:
                    continue
                dp[v | 1 << j] += dp[v]
                dp[v | 1 << j] %= MOD
    print(dp[2**N - 1])


def solve_ref(N: int, A: "List[List[int]]"):
    """https://atcoder.jp/contests/dp/submissions/34153826"""
    dp = [0] * (1 << N)
    dp[0] = 1

    # 0からincrementすると1が立っている数は0から始まって単調増加
    for bit in range(1 << N):
        c = 0
        m = bit
        while m:
            if m & 1:
                c += 1
            m = m >> 1
        male = c - 1
        for female in range(N):
            if A[male][female] and not bit & 1 << female:
                dp[bit | (1 << female)] += dp[bit]
                dp[bit | (1 << female)] %= MOD

    print(dp[-1])


def main():
    import sys

    sys.setrecursionlimit(10**9)

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)
    # solve_ref(N, A)


if __name__ == "__main__":
    main()
