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
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    T = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, S, T)


def solve(N: int, M: int, S: "List[str]", T: "List[str]"):
    ti = 0
    for s in S:
        if s == T[ti]:
            print("Yes")
            ti += 1
        else:
            print("No")


if __name__ == "__main__":
    main()
