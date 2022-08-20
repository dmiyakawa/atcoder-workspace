#!/usr/bin/env python3



def solve(N: int, M: int, K: int, P: "List[int]", X: "List[int]", Q: "List[int]", Y: "List[int]"):
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
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int()] * (K)  # type: "List[int]"
    X = [int()] * (K)  # type: "List[int]"
    Q = [int()] * (K)  # type: "List[int]"
    Y = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        P[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Q[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, K, P, X, Q, Y)


if __name__ == "__main__":
    main()
