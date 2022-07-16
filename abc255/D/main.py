#!/usr/bin/env python3

import bisect
import sys


def solve(N: int, Q: int, A: "List[int]", X: "List[int]"):
    A.sort()
    B = A.copy()
    for i in range(1, N):
        B[i] += B[i - 1]

    for x in X:
        i = bisect.bisect(A, x)
        a = i * x - (B[i - 1] if i > 0 else 0)
        b = B[N - 1] - (B[i - 1] if i > 0 else 0) - (N - i) * x
        # print(a + b, A, x, i, a, b)
        print(a + b)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    X = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, X)


if __name__ == "__main__":
    main()
