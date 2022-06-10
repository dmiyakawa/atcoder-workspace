#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, Q: int, S: "List[str]", X: "List[int]", T: "List[str]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    X = [int()] * (Q)  # type: "List[int]"
    T = [str()] * (Q)  # type: "List[str]"
    for i in range(Q):
        X[i] = int(next(tokens))
        T[i] = next(tokens)
    solve(N, Q, S, X, T)


if __name__ == "__main__":
    main()
