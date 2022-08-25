#!/usr/bin/env python3



def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    ai, bi = 0, 0
    C = []
    while ai < N or bi < M:
        if ai == N:
            C.append(B[bi])
            bi += 1
        elif bi == M:
            C.append(A[ai])
            ai += 1
        elif A[ai] <= B[bi]:
            C.append(A[ai])
            ai += 1
        else:
            C.append(B[bi])
            bi += 1
    for c in C:
        print(c)


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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A, B)


if __name__ == "__main__":
    main()
