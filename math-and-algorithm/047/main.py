#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    return


if __name__ == "__main__":
    main()
