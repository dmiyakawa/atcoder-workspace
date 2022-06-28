#!/usr/bin/env python3

import sys
from collections import Counter

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, a: "List[int]"):
    counter = Counter(a)
    ans = 0
    for key, value in counter.items():
        if value > key:
            ans += value - key
        elif value < key:
            ans += value
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
