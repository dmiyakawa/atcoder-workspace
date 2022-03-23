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
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, Q, L, R, X)


def solve(N: int, Q: int, L: "List[int]", R: "List[int]", X: "List[int]"):
    return


if __name__ == "__main__":
    main()
