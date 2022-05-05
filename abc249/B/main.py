#!/usr/bin/env python3

import sys

input = sys.stdin.readline
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
    S = next(tokens)  # type: str
    solve(S)


def solve(S: str):
    Uppers = set()
    Lowers = set()
    alls = set()
    for ch in S:
        if ch.isupper():
            Uppers.add(ch)
        if ch.islower():
            Lowers.add(ch)
        alls.add(ch)
    print(YES if Uppers and Lowers and len(alls) == len(S) else NO)


if __name__ == "__main__":
    main()
