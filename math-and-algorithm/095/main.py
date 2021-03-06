#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        C[i] = int(next(tokens))
        P[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, C, P, Q, L, R)


def solve(N: int, C: "List[int]", P: "List[int]", Q: int, L: "List[int]", R: "List[int]"):
    return


if __name__ == "__main__":
    main()
