#!/usr/bin/env python3


MOD = 998244353  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, K, W)


def solve(N: int, M: int, K: int, W: "List[int]"):
    return


if __name__ == "__main__":
    main()
