#!/usr/bin/env python3



def solve(N: int, A: "List[int]", B: "List[int]", Q: int, U: "List[int]", K: "List[int]"):
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
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    U = [int()] * (Q)  # type: "List[int]"
    K = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        U[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, A, B, Q, U, K)


if __name__ == "__main__":
    main()
