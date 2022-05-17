#!/usr/bin/env python3
import itertools
import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, W, A)


def solve(N: int, W: int, A: "List[int]"):
    A = sorted(A)
    s = set()
    for a in A:
        if a <= W:
            s.add(a)

    for a, b in itertools.combinations(A, 2):
        if a + b <= W:
            s.add(a + b)
    for a, b, c in itertools.combinations(A, 3):
        if a + b + c <= W:
            s.add(a + b + c)
    print(len(s))


if __name__ == "__main__":
    main()
