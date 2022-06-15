#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(X: int, Y: int, Z: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(X)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(Y)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(Z)]  # type: "List[int]"
    solve(X, Y, Z, K, A, B, C)


if __name__ == "__main__":
    main()
