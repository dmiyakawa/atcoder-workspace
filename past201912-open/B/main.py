#!/usr/bin/env python3

import sys

input = sys.stdin.readline
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
    solve(N, A)


def solve(N: int, A: "List[int]"):
    for i in range(1, N):
        diff = A[i] - A[i-1]
        if diff > 0:
            print("up {}".format(diff))
        elif diff < 0:
            print("down {}".format(abs(diff)))
        else:
            print("stay")


if __name__ == "__main__":
    main()
