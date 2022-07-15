#!/usr/bin/env python3

import sys

def solve(N: int):
    min_remainder = N
    for a in range(1, N + 1):
        b = N // a
        rem = N % a
        min_remainder = min(min_remainder, rem + abs(b - a))
    print(min_remainder)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    solve(n)


if __name__ == "__main__":
    main()
