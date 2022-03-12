#!/usr/bin/env python3


MOD = 7  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q, A)


def solve(N: int, P: int, Q: int, A: "List[int]"):
    return


if __name__ == "__main__":
    main()
