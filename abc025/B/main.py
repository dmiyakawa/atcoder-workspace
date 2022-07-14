#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: int, B: int, s: "List[str]", d: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    s = [str()] * (N)  # type: "List[str]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = next(tokens)
        d[i] = int(next(tokens))
    solve(N, A, B, s, d)


if __name__ == "__main__":
    main()
