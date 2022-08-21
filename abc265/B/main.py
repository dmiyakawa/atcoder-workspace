#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, T: int, A: "List[int]", X: "List[int]", Y: "List[int]"):
    d = {}
    for x, y in zip(X, Y):
        d[x - 1] = y
    t = T
    for i in range(N - 1):
        if i in d:
            t += d[i]
        if A[i] >= t:
            return False
        t -= A[i]
    return True


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
    T = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    print(YES if solve(N, M, T, A, X, Y) else NO)


if __name__ == "__main__":
    main()
