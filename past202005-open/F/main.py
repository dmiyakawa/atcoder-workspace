#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, a: "List[str]"):
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [next(tokens) for _ in range(2)]  # type: "List[str]"
    solve(N, a)


if __name__ == "__main__":
    main()
