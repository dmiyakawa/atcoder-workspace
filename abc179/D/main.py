#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int

def solve(N: int, K: int, L: "List[int]", R: "List[int]"):
    incl = [0 for _ in range(N)]
    inc = 0
    for i in range(N):
        inc = (inc + incl[i]) % MOD
        for l, r in zip(L, R):
            if i + l < N:
                incl[i + l] += inc if i > 0 else 1
            if i + r + 1 < N:
                incl[i + r + 1] -= inc if i > 0 else 1
    print(inc)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = [int()] * (K)  # type: "List[int]"
    R = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, K, L, R)





if __name__ == "__main__":
    main()
