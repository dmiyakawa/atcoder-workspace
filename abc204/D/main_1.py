#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, T: "List[int]"):
    a = 0
    b = 0
    for val in sorted(T, reverse=True):
        if sum(a) > sum(b):
            b.append(val)
        else:
            a.append(val)
    print(max(sum(a), sum(b)))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)


if __name__ == "__main__":
    main()
