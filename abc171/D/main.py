#!/usr/bin/env python3
from collections import Counter


def solve(N: int, A: "List[int]", Q: int, B: "List[int]", C: "List[int]"):
    counter = Counter(A)
    total = sum(A)
    for b, c in zip(B, C):
        counter[c] += counter[b]
        total = total - counter[b] * b + counter[b] * c
        del counter[b]
        print(total)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = int(next(tokens))  # type: int
    B = [int()] * (Q)  # type: "List[int]"
    C = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, A, Q, B, C)





if __name__ == "__main__":
    main()
