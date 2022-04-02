#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A_x = int(next(tokens))  # type: int
    A_y = int(next(tokens))  # type: int
    B_x = int(next(tokens))  # type: int
    B_y = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, A_x, A_y, B_x, B_y, S)


def solve(N: int, A_x: int, A_y: int, B_x: int, B_y: int, S: "List[str]"):
    if (A_x + A_y) % 2 != (B_x + B_y) % 2:
        print(-1)
        return

    print(1)


if __name__ == "__main__":
    main()
