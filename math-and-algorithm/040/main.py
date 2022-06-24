#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, A, M, B)


def solve(N: int, A: "List[int]", M: int, B: "List[int]"):
    total = 0
    C = [0]
    total = 0
    for a in A:
        total += a
        C.append(total)
    total = 0
    for i in range(1, M):
        cur = B[i] - 1
        prev = B[i - 1] - 1
        total += abs(C[cur] - C[prev])
    print(total)


if __name__ == "__main__":
    main()
