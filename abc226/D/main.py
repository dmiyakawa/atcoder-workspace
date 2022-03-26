#!/usr/bin/env python3

import math
import itertools


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


def solve(N: int, x: "List[int]", y: "List[int]"):
    combs = set()
    for (x1, y1), (x2, y2) in itertools.permutations(zip(x, y), 2):
        a = abs(math.gcd(x1 - x2, y1 - y2))
        combs.add(((x1 - x2) // a, (y1 - y2) // a))
        combs.add(((x2 - x1) // a, (y2 - y1) // a))

    print(len(combs))


if __name__ == "__main__":
    main()
