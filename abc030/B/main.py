#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(n: int, m: int):
    n = n % 12
    hour_hand = 360 * n // 12 + 30 * m / 60
    min_hand = 360 * m // 60
    ans = abs(hour_hand - min_hand)
    if ans > 180:
        ans = 360 - ans
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    solve(n, m)


if __name__ == "__main__":
    main()
