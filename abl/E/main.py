#!/usr/bin/env python3

MOD = 998244353  # type: int


def solve(N: int, Q: int, L: "List[int]", R: "List[int]", D: "List[int]"):
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
    Q = int(next(tokens))  # type: int
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, Q, L, R, D)


if __name__ == "__main__":
    main()
