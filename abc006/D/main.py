#!/usr/bin/env python3

import sys
from typing import List

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
    c = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, c)


def solve(N: int, c: "List[int]"):
    import bisect
    # Longest Increasing Sequenceを見つける
    seq = [Inf] * (N + 1)
    seq[0] = -Inf
    max_index = -Inf
    for ci in c:
        index = bisect.bisect_left(seq, ci)
        seq[index] = ci
        max_index = max(index, max_index)
    print(N - max_index)


if __name__ == "__main__":
    main()
