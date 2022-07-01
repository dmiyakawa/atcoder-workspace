#!/usr/bin/env python3

import sys

def match(N, M, A, B, x, y) -> bool:
    for i in range(M):
        for j in range(M):
            if A[i + x][j + y] != B[i][j]:
                return False
    return True

def solve(N: int, M: int, A: "List[str]", B: "List[str]"):
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            if match(N, M, A, B, x, y):
                print("Yes")
                return
    print("No")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    B = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, A, B)


if __name__ == "__main__":
    main()
