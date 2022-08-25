#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]"):
    prev = None
    n = -1
    lst = []
    for a, i in sorted((a, i) for i, a in enumerate(A)):
        if prev != a:
            n += 1
        lst.append((n, i))
        prev = a
    for b, _ in sorted(lst, key=lambda tup: tup[1]):
        print(b)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
