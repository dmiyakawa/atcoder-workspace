#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    X = [float()] * (Q)  # type: "List[float]"
    Y = [float()] * (Q)  # type: "List[float]"
    Z = [float()] * (Q)  # type: "List[float]"
    T = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        X[i] = float(next(tokens))
        Y[i] = float(next(tokens))
        Z[i] = float(next(tokens))
        T[i] = int(next(tokens))
    solve(Q, X, Y, Z, T)


def solve(Q: int, X: "List[float]", Y: "List[float]", Z: "List[float]", T: "List[int]"):
    return


if __name__ == "__main__":
    main()
