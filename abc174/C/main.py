#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(K: int):
    rem = 0
    for n in range(1, 10**6):
        rem = (rem * 10 + 7) % K
        if rem == 0:
            print(n)
            return
    print(-1)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == "__main__":
    main()
