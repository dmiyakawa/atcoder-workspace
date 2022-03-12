#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, Q, A, X, Y)


def solve(N: int, Q: int, A: "List[int]", X: "List[int]", Y: "List[int]"):
    return


if __name__ == "__main__":
    main()
