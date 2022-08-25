#!/usr/bin/env python3



def solve(N: int, K: int, M: int, A: "List[int]", B: "List[int]", Q: int, S: "List[int]", T: "List[int]"):
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
    K = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    S = [int()] * (Q)  # type: "List[int]"
    T = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(N, K, M, A, B, Q, S, T)


if __name__ == "__main__":
    main()
