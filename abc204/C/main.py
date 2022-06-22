#!/usr/bin/env python3

import sys
from collections import defaultdict


def solve(N: int, M: int, A, B):
    d = defaultdict(set)
    for a, b in zip(A, B):
        d[a].add(b)

    count = 0
    for n in range(1, N + 1):
        _visited = set()
        to_visit = {n}
        while to_visit:
            current = to_visit.pop()
            _visited.add(current)
            for _m in d[current]:
                if _m in _visited:
                    continue
                to_visit.add(_m)
        count += len(_visited)
    print(count)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == "__main__":
    main()
