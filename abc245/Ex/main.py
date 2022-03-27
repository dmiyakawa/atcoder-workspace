#!/usr/bin/env python3


MOD = 998244353  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(K, N, M)


def solve(K: int, N: int, M: int):
    return


if __name__ == "__main__":
    main()
