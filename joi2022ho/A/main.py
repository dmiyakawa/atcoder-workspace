#!/usr/bin/env python3

import bisect


def solve(N: int, A: "List[int]", Q: int, X: "List[int]"):
    B = []
    C = []
    total = 0
    for a in A:
        n = 1
        v = a
        while v % 2 == 0:
            n *= 2
            v //= 2
        total += n
        B.append(v)
        C.append(total)
    # print(B)
    # print(C)
    for x in X:
        i = bisect.bisect_left(C, x)
        print(B[i])

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
    Q = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, A, Q, X)


if __name__ == "__main__":
    main()
