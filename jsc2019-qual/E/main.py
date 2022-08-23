#!/usr/bin/env python3



def solve(N: int, H: int, W: int, R: "List[int]", C: "List[int]", A: "List[int]"):
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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    R = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        R[i] = int(next(tokens))
        C[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, H, W, R, C, A)


if __name__ == "__main__":
    main()
