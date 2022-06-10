#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, P: "List[str]", V: "List[str]"):
    d = {}
    for i, (p, v) in enumerate(zip(P, V), start=1):
        if v == "AC" and p not in d:
            d[p] = i
    for p in "ABCDEF":
        print(d[p])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [str()] * (N)  # type: "List[str]"
    V = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        P[i] = next(tokens)
        V[i] = next(tokens)
    solve(N, P, V)


if __name__ == "__main__":
    main()
