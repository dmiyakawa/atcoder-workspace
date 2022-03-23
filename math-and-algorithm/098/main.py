#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, X, Y, A, B)


def solve(N: int, X: "List[int]", Y: "List[int]", A: int, B: int):
    return


if __name__ == "__main__":
    main()
