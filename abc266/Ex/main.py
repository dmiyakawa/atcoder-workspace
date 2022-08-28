#!/usr/bin/env python3



def solve(N: int, T: "List[int]", X: "List[int]", Y: "List[int]", A: "List[int]"):
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
    T = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, T, X, Y, A)


if __name__ == "__main__":
    main()
