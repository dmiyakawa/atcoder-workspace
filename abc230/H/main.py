#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    w = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(W, K, w)


def solve(W: int, K: int, w: "List[int]"):
    return


if __name__ == "__main__":
    main()
