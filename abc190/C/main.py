#!/usr/bin/env python3

import sys

def solve(N: int, M: int, A: "List[int]", B: "List[int]", K: int, C: "List[int]", D: "List[int]"):
    max_count = 0
    for n in range(2**16):
        selected = set()
        for j, (c, d) in enumerate(zip(C, D)):
            selected.add(d if n >> j & 1 else c)
        count = 0
        for a, b in zip(A, B):
            if a in selected and b in selected:
                count += 1
        max_count = max(max_count, count)
    print(max_count)


def main():

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
    K = int(next(tokens))  # type: int
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, A, B, K, C, D)


if __name__ == "__main__":
    main()
