#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    C = [int()] * (M)  # type: "List[int]"
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, C, L, R)


def solve(N: int, M: int, C: "List[int]", L: "List[int]", R: "List[int]"):
    return


if __name__ == "__main__":
    main()
