#!/usr/bin/env python3


MOD = 10  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


def solve(N: int, K: int):
    return


if __name__ == "__main__":
    main()
