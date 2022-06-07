#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 2  # type: int


def solve(k: int, q: int, d: "List[int]", n: "List[int]", x: "List[int]", m: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    k = int(next(tokens))  # type: int
    q = int(next(tokens))  # type: int
    d = [int(next(tokens)) for _ in range(k)]  # type: "List[int]"
    n = [int()] * (q)  # type: "List[int]"
    x = [int()] * (q)  # type: "List[int]"
    m = [int()] * (q)  # type: "List[int]"
    for i in range(q):
        n[i] = int(next(tokens))
        x[i] = int(next(tokens))
        m[i] = int(next(tokens))
    solve(k, q, d, n, x, m)


if __name__ == "__main__":
    main()
