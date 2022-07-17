#!/usr/bin/env python3

import sys
from collections import Counter

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(S: str):
    counter = Counter(S)
    for key, value in counter.items():
        if value == 1:
            print(key)
            return
    print(-1)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
