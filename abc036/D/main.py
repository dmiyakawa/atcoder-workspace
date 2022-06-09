#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]", B: "List[int]"):
    # んあー
    d = {}
    patterns = {}
    for a, b in zip(A, B):
        d.setdefault(a - 1, set()).add(b - 1)
        d.setdefault(b - 1, set()).add(a - 1)
    to_be_processed = {i for i in range(N)}


    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == "__main__":
    main()
