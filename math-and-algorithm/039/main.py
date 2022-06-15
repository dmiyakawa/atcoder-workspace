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
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, Q, L, R, X)


def solve(N: int, Q: int, L: "List[int]", R: "List[int]", X: "List[int]"):
    lst = [0] * N
    for l, r, x in zip(L, R, X):
        if l > 0:
            lst[l - 1] += x
        if r < N:
            lst[r] -= x
    result = []
    for val in lst[1:]:
        result.append("<" if val > 0 else (">" if val < 0 else "="))
    print("".join(result))


if __name__ == "__main__":
    main()
