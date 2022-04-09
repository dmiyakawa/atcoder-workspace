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
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    print(YES if solve(N, X, a, b) else NO)


def solve(N: int, X: int, a: "List[int]", b: "List[int]"):
    possible_positions = {0}
    for ai, bi in zip(a, b):
        next_positions = set()
        for p in possible_positions:
            if p + ai <= X:
                next_positions.add(p + ai)
            if p + bi <= X:
                next_positions.add(p + bi)
        possible_positions = next_positions
    return X in possible_positions


if __name__ == "__main__":
    main()
