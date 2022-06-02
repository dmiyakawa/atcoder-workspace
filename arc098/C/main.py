#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


def solve(N: int, S: str):
    num_wests = []
    num_easts = []
    num_west = 0
    num_east = 0
    for ch in S:
        if ch == "W":
            num_west += 1
        else:
            num_east += 1
        num_wests.append(num_west)
        num_easts.append(num_east)
    distracted_totals = []
    for i in range(N):
        num_distracted = 0
        if i > 0:
            num_distracted += num_wests[i - 1]
        num_distracted += num_easts[N - 1] - num_easts[i]
        distracted_totals.append(num_distracted)
    print(min(distracted_totals))


if __name__ == "__main__":
    main()
