#!/usr/bin/env python3

MOD = 1000000007  # type: int


def solve(N: int, A: int, B: int, S: "List[int]"):
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
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, S)


if __name__ == "__main__":
    main()
