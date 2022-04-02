#!/usr/bin/env python3
import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


def solve(N: int):
    min_n = INF
    m = math.ceil(math.pow(N, 1 / 3))
    for a in range(m, 0, -1):
        for b in range(a - 1000000, a):
            if (a**2 + b**2) * (a + b) < N:
                break
            min_n = min(min_n, (a**2 + b**2)*(a + b))
            if min_n == N:
                break
        if min_n == N:
            break
    print(min_n)


if __name__ == "__main__":
    main()
