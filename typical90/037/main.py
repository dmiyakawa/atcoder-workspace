#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    V = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(W, N, L, R, V)


def solve(W: int, N: int, L: "List[int]", R: "List[int]", V: "List[int]"):
    return


if __name__ == "__main__":
    main()
