#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "yes"  # type: str
NO = "no"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(T, N, A, M, B)


def solve(T: int, N: int, A: "List[int]", M: int, B: "List[int]"):
    a_i = 0
    soldable = True
    for b in B:
        while a_i < len(A) and A[a_i] + T < b:
            a_i += 1
        if a_i < len(A) and A[a_i] <= b:
            a_i += 1
        else:
            soldable = False
            break
    print("yes" if soldable else "no")


if __name__ == "__main__":
    main()
