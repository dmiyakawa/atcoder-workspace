#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, S, D, X, Y)


def solve(N: int, S: int, D: int, X: "List[int]", Y: "List[int]"):
    ok = False
    for x, y in zip(X, Y):
        if x < S and D < y:
            ok = True
            break
    print(YES if ok else NO)


if __name__ == "__main__":
    main()
