#!/usr/bin/env python3
from bisect import bisect
from collections import defaultdict


def solve(N: int, A: "List[int]"):
    B = sorted(set(A))
    d = defaultdict(list)
    for a in A:
        i = bisect(B, a)
        d[len(B) - i].append(a)

    for i in range(N):
        print(len(d.get(i, set())))



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
