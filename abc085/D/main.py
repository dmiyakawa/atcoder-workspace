#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, H: int, a: "List[int]", b: "List[int]"):
    a_max = max(a)
    b.sort(reverse=True)
    remaining = H
    count = 0
    for value in b:
        if remaining <= 0 or value < a_max:
            break
        remaining -= value
        count += 1

    if remaining > 0:
        count += remaining // a_max + (1 if remaining % a_max > 0 else 0)

    print(count)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, H, a, b)


if __name__ == "__main__":
    main()
