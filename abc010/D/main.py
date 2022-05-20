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
    G = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(G)]  # type: "List[int]"
    a = [int()] * (E)  # type: "List[int]"
    b = [int()] * (E)  # type: "List[int]"
    for i in range(E):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, G, E, p, a, b)


def solve(N: int, G: int, E: int, p: "List[int]", a: "List[int]", b: "List[int]"):
    return


if __name__ == "__main__":
    main()
