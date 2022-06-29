#!/usr/bin/env python3

import sys
from collections import defaultdict


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    d = defaultdict(set)
    for a, b in zip(A, B):
        d[a].add(b)
        d[b].add(a)
    visited = set()
    to_visit = {(1, 1)}
    while to_visit:
        n, m = to_visit.pop()
        if n in visited:
            continue
        visited.add(n)
        if m <= 2:
            for next_n in d[n]:
                if next_n not in visited:
                    to_visit.add((next_n, m + 1))
    print("POSSIBLE" if N in visited else "IMPOSSIBLE")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == "__main__":
    main()
