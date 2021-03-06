#!/usr/bin/env python3

import sys
from collections import Counter

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
    counter = Counter(A)
    print(sum(v - 1 for v in counter.values()))


if __name__ == "__main__":
    main()
