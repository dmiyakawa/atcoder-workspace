#!/usr/bin/env python3

import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    s = sum(A)
    C = sorted([2 * a + b for a, b in zip(A, B)], reverse=True)
    ans = 0
    for c in C:
        # print(s, c, s - c)
        s -= c
        ans += 1
        if s < 0:
            break
    print(ans)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == "__main__":
    main()
