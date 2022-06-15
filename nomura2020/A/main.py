#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(H: "List[int]", M: "List[int]", K: int):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = [int()] * (2)  # type: "List[int]"
    M = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        H[i] = int(next(tokens))
        M[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    solve(H, M, K)


if __name__ == "__main__":
    main()
