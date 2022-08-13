#!/usr/bin/env python3

import sys


def solve(R: int, C: int):
    table = [[0] * 15 for _ in range(15)]
    for n in range(0, 8, 2):
        for i in range(n, 15 - n):
            table[n][i] = 1
            table[14 - n][i] = 1
            table[i][n] = 1
            table[i][14 - n] = 1
    print("black" if table[R - 1][C - 1] else "white")

def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(R, C)


if __name__ == "__main__":
    main()
