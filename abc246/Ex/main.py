#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


MOD = 998244353  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    x = [int()] * (Q)  # type: "List[int]"
    c = [str()] * (Q)  # type: "List[str]"
    for i in range(Q):
        x[i] = int(next(tokens))
        c[i] = next(tokens)
    solve(N, Q, S, x, c)


def solve(N: int, Q: int, S: str, x: "List[int]", c: "List[str]"):
    return


if __name__ == "__main__":
    main()
