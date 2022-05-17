#!/usr/bin/env python3

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
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    # solve(N, M, A, B)
    solve2(A, B)


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    A.sort()
    B.sort()
    ai = 0
    bi = 0
    ans = Inf
    while ai < len(A) and bi < len(B):
        ans = min(ans, abs(A[ai] - B[bi]))
        if A[ai] < B[bi]:
            ai += 1
        else:
            bi += 1
    print(ans)


def solve2(A: "List[int]", B: "List[int]"):
    import bisect
    B.sort()
    ans = Inf
    for a in A:
        bi = bisect.bisect(B, a)
        if bi > 0:
            ans = min(ans, abs(a - B[bi - 1]))
        if bi < len(B):
            ans = min(ans, abs(a - B[bi]))
    print(ans)


if __name__ == "__main__":
    main()
