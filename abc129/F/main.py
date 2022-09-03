#!/usr/bin/env python3

MOD = 10007  # type: int


def solve(L: int, A: int, B: int, M: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(L, A, B, M)


if __name__ == "__main__":
    main()
