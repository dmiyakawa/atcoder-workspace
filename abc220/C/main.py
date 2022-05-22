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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    X = int(next(tokens))  # type: int
    solve(N, A, X)


def solve(N: int, A: "List[int]", X: int):
    a_total = sum(A)
    count = (X // a_total) * N
    X = X % a_total
    i = 0
    while X >= 0:
        X -= A[i]
        count += 1
        i += 1
    print(count)


if __name__ == "__main__":
    main()
