#!/usr/bin/env python3

import itertools
import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str

def is_same(A, B, H2, W2, row, col):
    for i in range(H2):
        for j in range(W2):
            if A[row[i]][col[j]] != B[i][j]:
                return False
    return True


def solve(H1, W1, A, H2, W2, B):
    for row in itertools.combinations([i for i in range(H1)], H2):
        for col in itertools.combinations([i for i in range(W1)], W2):
            if is_same(A, B, H2, W2, row, col):
                return True
    return False


def main():
    H1, W1 = map(int, input().split())
    A = [[int(e) for e in input().split()] for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [[int(e) for e in input().split()] for _ in range(H2)]
    print(YES if solve(H1, W1, A, H2, W2, B) else NO)


if __name__ == "__main__":
    main()
