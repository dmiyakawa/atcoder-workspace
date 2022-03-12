#!/usr/bin/env python3


MOD = 998244353  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    solve(R, G, B, K, X, Y, Z)


def solve(R: int, G: int, B: int, K: int, X: int, Y: int, Z: int):
    return


if __name__ == "__main__":
    main()
