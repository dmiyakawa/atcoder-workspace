#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[str]"):
    for i in range(N):
        for j in range(N):
            if A[i][j] == "W":
                if A[j][i] != "L":
                    return False
            elif A[i][j] == "L":
                if A[j][i] != "W":
                    return False
            elif A[i][j] == "D":
                if A[j][i] != "D":
                    return False
    return True


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    print("correct" if solve(N, A) else "incorrect")


if __name__ == "__main__":
    main()
