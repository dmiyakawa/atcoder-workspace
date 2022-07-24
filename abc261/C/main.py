#!/usr/bin/env python3

import sys
from collections import Counter

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, S: "List[str]"):
    d = {}
    for s in S:
        if s in d:
            postfix = "({})".format(d[s])
        else:
            postfix = ""
        print("{}{}".format(s, postfix))
        d[s] = d.get(s, 0) + 1


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == "__main__":
    main()
