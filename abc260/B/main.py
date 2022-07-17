#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, X: int, Y: int, Z: int, A: "List[int]", B: "List[int]"):
    C = []
    p = set()
    for n, (a, b) in enumerate(zip(A, B), start=1):
        C.append((a, b, n))

    rem = X
    for tup in sorted(C, key=lambda t: -t[0]):
        if rem == 0:
            break
        if tup not in p:
            p.add(tup)
            rem -= 1
    rem = Y
    for tup in sorted(C, key=lambda t: -t[1]):
        if rem == 0:
            break
        if tup not in p:
            p.add(tup)
            rem -= 1
    rem = Z
    for tup in sorted(C, key=lambda t: (-t[0] - t[1], t[2])):
        if rem == 0:
            break
        if tup not in p:
            p.add(tup)
            rem -= 1
    for tup in sorted(p, key=lambda t: t[2]):
        print(tup[2])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, Y, Z, A, B)


if __name__ == "__main__":
    main()
