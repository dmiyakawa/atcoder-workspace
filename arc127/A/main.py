#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int):
    count = 0
    for m in range(1, len(str(N)) + 1):
        for mm in range(1, m + 1):
            low = int("1" * mm + "0" * (m - mm))
            if N >= low:
                high = min(N, int("1" * mm + "9" * (m - mm)))
                count += high - low + 1
    print(count)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
