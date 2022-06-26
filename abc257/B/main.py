#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, Q: int, A: "List[int]", L: "List[int]"):
    for l in L:
        if A[l - 1] == N  or (l < K and A[l - 1] + 1 == A[l]):
            continue
        A[l - 1] += 1
    print(*A)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    L = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A, L)


if __name__ == "__main__":
    main()
