#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    K = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, x, y, Q, a, b, K)


def solve(N: int, x: "List[int]", y: "List[int]", Q: int, a: "List[int]", b: "List[int]", K: "List[int]"):
    return


if __name__ == "__main__":
    main()
