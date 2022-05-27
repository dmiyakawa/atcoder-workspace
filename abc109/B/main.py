#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, W)


def solve(N: int, W: "List[str]"):
    return


if __name__ == "__main__":
    main()
