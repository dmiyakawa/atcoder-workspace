#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(T)]  # type: "List[str]"
    solve(T, S)


def solve(T: int, S: "List[str]"):
    return


if __name__ == "__main__":
    main()
