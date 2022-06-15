#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, Q, A, L, R)


def solve(N: int, Q: int, A: "List[int]", L: "List[int]", R: "List[int]"):
    Asum = []
    total = 0
    for a in A:
        total += a
        Asum.append(total)
    for l, r in zip(L, R):
        print(Asum[r - 1] - (Asum[l - 2] if l - 2 >= 0 else 0))


if __name__ == "__main__":
    main()
