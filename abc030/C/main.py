#!/usr/bin/env python3

import sys
from bisect import bisect_left

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, M: int, X: int, Y: int, a: "List[int]", b: "List[int]"):
    c = []
    for a0 in a:
        i = bisect_left(b, a0 + X)
        if i < M:
            c.append((b[i] + Y, a0))
    c.sort()
    cnt = 0
    cd = 0
    for d, s in c:
        if cd <= s:
            cd = d
            cnt += 1
    print(cnt)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X, Y, a, b)


if __name__ == "__main__":
    main()
