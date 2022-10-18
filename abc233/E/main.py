#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(X: str):
    N = len(X)
    Y = [int(ch) for ch in X]
    Z = Y.copy()
    for i in range(1, N):
        Z[i] += Z[i - 1]
    rev = []
    rem = 0
    for i in range(N - 1, -1, -1):
        v = Z[i] + rem
        rev.append(str(v % 10))
        rem = v // 10
    while rem:
        rev.append(str(rem % 10))
        rem //= 10
    rev.reverse()
    print("".join(rev))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = next(tokens)  # type: str
    solve(X)





if __name__ == "__main__":
    main()
