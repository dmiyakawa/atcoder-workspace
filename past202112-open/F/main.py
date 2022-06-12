#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(A: int, B: int, S: "List[str]"):
    A, B = A - 1, B - 1
    visited = {(A, B)}
    checked = {(A, B)}
    to_check = [(A, B)]
    movable = []
    for i, lst in enumerate(S, start=-1):
        for j, ch in enumerate(lst, start=-1):
            if ch == "#":
                movable.append((i, j))
    while to_check:
        x, y = to_check.pop()
        visited.add((x, y))
        for a, b in movable:
            x0, y0 = x + a, y + b
            if 0 <= x0 < 9 and 0 <= y0 < 9 and (x0, y0) not in checked:
                to_check.append((x0, y0))
            checked.add((x0, y0))
    print(len(visited))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(A, B, S)


if __name__ == "__main__":
    main()
