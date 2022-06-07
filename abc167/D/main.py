#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, A: "List[int]"):
    import math
    # 周期性ではなくダブリングで解いてみる
    doubling = [[a - 1 for a in A]]
    for k in range(1, math.ceil(math.log2(K))):
        doubling.append([])
        for j in range(N):
            doubling[k].append(doubling[k - 1][doubling[k - 1][j]])
    p = 0
    while math.log2(K) > 10:
        k = math.floor(math.log2(K))
        p = doubling[k][p]
        K -= 2**k
    for i in range(K):
        p = doubling[0][p]
    print(p + 1)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == "__main__":
    main()
