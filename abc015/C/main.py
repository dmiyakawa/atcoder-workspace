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
    K = int(next(tokens))  # type: int
    T = [[int(next(tokens)) for _ in range(K)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, K, T)


def solve(N: int, K: int, T: "List[List[int]]"):
    from functools import reduce
    from itertools import product
    found = False
    for tup in product(*T):
        if reduce(lambda x, y: x ^ y, tup) == 0:
            found = True
    print("Found" if found else "Nothing")


if __name__ == "__main__":
    main()
