#!/usr/bin/env python3

from functools import reduce
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, C: "List[List[int]]"):
    D = []
    max_d = -10**9 - 1
    max_d_i = 0
    for i0 in range(N):
        i1 = (i0 + 1) % N
        if not reduce(lambda x, y: x == y, [x - y for x, y in zip(C[i0], C[i1])]):
            print("No")
            return
        d = C[i0][0] - C[i1][0]
        D.append(d)
        if max_d < d:
            max_d = d
            max_d_i = i0
    if min(b - max_d for b in C[max_d_i]) < 0:
        print("No")
        return




def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, C)


if __name__ == "__main__":
    main()
