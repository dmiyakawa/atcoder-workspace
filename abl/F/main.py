#!/usr/bin/env python3

MOD = 998244353  # type: int


def solve(N: int, h: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, h)


if __name__ == "__main__":
    main()
