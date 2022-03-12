#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, Q, X, Y, A, B)


def solve(N: int, M: int, Q: int, X: "List[int]", Y: "List[int]", A: "List[int]", B: "List[int]"):
    return


if __name__ == "__main__":
    main()
