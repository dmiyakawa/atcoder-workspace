#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, A: "List[List[int]]"):
    total_max = 0
    for i in range(M):
        for j in range(i + 1, M):
            total_max = max(total_max, sum(max(a[i], a[j]) for a in A))
    print(total_max)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(M)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
