#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(Q, X, Y, A, B)


def solve(Q: int, X: "List[int]", Y: "List[int]", A: "List[int]", B: "List[int]"):
    return


if __name__ == "__main__":
    main()
