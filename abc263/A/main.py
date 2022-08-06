#!/usr/bin/env python3

import sys
from collections import Counter

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: int, B: int, C: int, D: int, E: int):
    lst = [A, B, C, D, E]
    c = Counter(lst)
    values = sorted(c.values())
    print("Yes" if len(values) == 2 and values[0] == 2 and values[1] == 3 else "No")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(A, B, C, D, E)


if __name__ == "__main__":
    main()
